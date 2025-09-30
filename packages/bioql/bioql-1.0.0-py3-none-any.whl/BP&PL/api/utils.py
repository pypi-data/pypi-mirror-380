"""
Utility functions for API endpoints.
"""

from flask import request, jsonify, current_app
from functools import wraps
import time
from typing import List, Dict, Any, Optional

from ..main import get_redis_client


def api_response(data: Any = None, message: str = None, status_code: int = 200) -> tuple:
    """
    Standardized API response format.

    Args:
        data: Response data
        message: Response message
        status_code: HTTP status code

    Returns:
        Tuple of (response, status_code)
    """
    response = {
        'success': status_code < 400,
        'timestamp': time.time()
    }

    if message:
        response['message'] = message

    if data is not None:
        response['data'] = data

    if status_code >= 400:
        response['error'] = True

    return jsonify(response), status_code


def validate_json(required_fields: List[str], optional_fields: List[str] = None):
    """
    Decorator to validate JSON request data.

    Args:
        required_fields: List of required field names
        optional_fields: List of optional field names

    Returns:
        Decorator function
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not request.is_json:
                return api_response(None, "Request must be JSON", 400)

            data = request.get_json()
            if not data:
                return api_response(None, "Request body cannot be empty", 400)

            # Check required fields
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return api_response(
                    None,
                    f"Missing required fields: {', '.join(missing_fields)}",
                    400
                )

            # Validate field types and values
            for field in required_fields:
                if not data[field]:  # Check for empty strings, None, etc.
                    return api_response(None, f"Field '{field}' cannot be empty", 400)

            return f(*args, **kwargs)

        return decorated
    return decorator


def rate_limit(key: str, limit: int, window: int):
    """
    Rate limiting decorator using Redis.

    Args:
        key: Rate limit key prefix
        limit: Maximum number of requests
        window: Time window in seconds

    Returns:
        Decorator function
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            redis_client = get_redis_client()

            if not redis_client:
                # If Redis is not available, allow the request
                return f(*args, **kwargs)

            # Create rate limit key
            client_ip = request.remote_addr
            rate_key = f"rate_limit:{key}:{client_ip}"

            try:
                current_requests = redis_client.get(rate_key)
                if current_requests is None:
                    # First request in window
                    redis_client.setex(rate_key, window, 1)
                    return f(*args, **kwargs)

                current_requests = int(current_requests)
                if current_requests >= limit:
                    return api_response(
                        None,
                        f"Rate limit exceeded. Maximum {limit} requests per {window} seconds.",
                        429
                    )

                # Increment counter
                redis_client.incr(rate_key)
                return f(*args, **kwargs)

            except Exception as e:
                current_app.logger.warning(f"Rate limiting error: {str(e)}")
                # If rate limiting fails, allow the request
                return f(*args, **kwargs)

        return decorated
    return decorator


def paginate_query(query, page: int = 1, per_page: int = 20, max_per_page: int = 100):
    """
    Paginate SQLAlchemy query.

    Args:
        query: SQLAlchemy query object
        page: Page number (1-based)
        per_page: Items per page
        max_per_page: Maximum items per page

    Returns:
        Dictionary with pagination data
    """
    # Validate and limit parameters
    page = max(1, page)
    per_page = min(max(1, per_page), max_per_page)

    # Calculate offset
    offset = (page - 1) * per_page

    # Get total count
    total = query.count()

    # Get paginated results
    items = query.offset(offset).limit(per_page).all()

    # Calculate pagination info
    total_pages = (total + per_page - 1) // per_page
    has_next = page < total_pages
    has_prev = page > 1

    return {
        'items': [item.to_dict() if hasattr(item, 'to_dict') else item for item in items],
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': total_pages,
            'has_next': has_next,
            'has_prev': has_prev,
            'next_page': page + 1 if has_next else None,
            'prev_page': page - 1 if has_prev else None
        }
    }


def get_pagination_params():
    """
    Extract pagination parameters from request.

    Returns:
        Tuple of (page, per_page)
    """
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
    except (ValueError, TypeError):
        page = 1
        per_page = 20

    return page, per_page


def filter_dict(data: Dict[str, Any], allowed_fields: List[str]) -> Dict[str, Any]:
    """
    Filter dictionary to only include allowed fields.

    Args:
        data: Input dictionary
        allowed_fields: List of allowed field names

    Returns:
        Filtered dictionary
    """
    return {k: v for k, v in data.items() if k in allowed_fields}


def validate_uuid(uuid_string: str) -> bool:
    """
    Validate UUID string format.

    Args:
        uuid_string: UUID string to validate

    Returns:
        True if valid UUID format
    """
    import re
    uuid_pattern = re.compile(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        re.IGNORECASE
    )
    return bool(uuid_pattern.match(uuid_string))


def validate_email(email: str) -> bool:
    """
    Validate email address format.

    Args:
        email: Email address to validate

    Returns:
        True if valid email format
    """
    import re
    email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    return bool(email_pattern.match(email))


def safe_float(value: Any, default: float = 0.0) -> float:
    """
    Safely convert value to float.

    Args:
        value: Value to convert
        default: Default value if conversion fails

    Returns:
        Float value or default
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def safe_int(value: Any, default: int = 0) -> int:
    """
    Safely convert value to integer.

    Args:
        value: Value to convert
        default: Default value if conversion fails

    Returns:
        Integer value or default
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def format_currency(amount: float, currency: str = 'USD') -> str:
    """
    Format amount as currency string.

    Args:
        amount: Amount to format
        currency: Currency code

    Returns:
        Formatted currency string
    """
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'CAD': 'C$'
    }

    symbol = currency_symbols.get(currency, currency)
    return f"{symbol}{amount:.2f}"


def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """
    Calculate percentage change between two values.

    Args:
        old_value: Original value
        new_value: New value

    Returns:
        Percentage change
    """
    if old_value == 0:
        return 100.0 if new_value > 0 else 0.0

    return ((new_value - old_value) / old_value) * 100


def generate_report_filename(report_type: str, user_id: str = None,
                           start_date: str = None, end_date: str = None) -> str:
    """
    Generate filename for downloadable reports.

    Args:
        report_type: Type of report
        user_id: User ID (optional)
        start_date: Start date string (optional)
        end_date: End date string (optional)

    Returns:
        Generated filename
    """
    from datetime import datetime

    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    filename_parts = ['bioql', report_type]

    if user_id:
        filename_parts.append(user_id[:8])  # Short user ID

    if start_date and end_date:
        filename_parts.extend([start_date, 'to', end_date])

    filename_parts.append(timestamp)

    return '_'.join(filename_parts) + '.csv'


def serialize_datetime(dt) -> Optional[str]:
    """
    Serialize datetime object to ISO format string.

    Args:
        dt: Datetime object

    Returns:
        ISO format string or None
    """
    if dt:
        return dt.isoformat()
    return None


def parse_date_range(start_date_str: str = None, end_date_str: str = None):
    """
    Parse date range strings into datetime objects.

    Args:
        start_date_str: Start date string (YYYY-MM-DD)
        end_date_str: End date string (YYYY-MM-DD)

    Returns:
        Tuple of (start_date, end_date) datetime objects
    """
    from datetime import datetime, timedelta

    try:
        if start_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        else:
            # Default to 30 days ago
            start_date = datetime.utcnow() - timedelta(days=30)

        if end_date_str:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            # Set to end of day
            end_date = end_date.replace(hour=23, minute=59, second=59)
        else:
            # Default to now
            end_date = datetime.utcnow()

        return start_date, end_date

    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD format.")


def create_csv_response(data: List[Dict], filename: str):
    """
    Create CSV response from list of dictionaries.

    Args:
        data: List of dictionaries to convert to CSV
        filename: Filename for download

    Returns:
        Flask response object
    """
    import csv
    import io
    from flask import Response

    if not data:
        return api_response(None, "No data available for export", 404)

    # Create CSV content
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    # Create response
    csv_content = output.getvalue()
    output.close()

    response = Response(
        csv_content,
        mimetype='text/csv',
        headers={
            'Content-Disposition': f'attachment; filename={filename}',
            'Content-Type': 'text/csv; charset=utf-8'
        }
    )

    return response