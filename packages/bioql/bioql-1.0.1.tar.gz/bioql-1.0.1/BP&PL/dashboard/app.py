"""
Flask web application for BioQL billing admin dashboard.
"""

from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
import requests
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = os.environ.get('DASHBOARD_SECRET_KEY', 'change-this-in-production')

# Configuration
API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:8000/api/v1')
DASHBOARD_PORT = int(os.environ.get('DASHBOARD_PORT', 5000))


def make_api_request(endpoint, method='GET', data=None, token=None):
    """Make authenticated API request."""
    headers = {'Content-Type': 'application/json'}

    if token:
        headers['Authorization'] = f'Bearer {token}'

    url = f"{API_BASE_URL}{endpoint}"

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, params=data)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)

        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}, 500


@app.route('/')
def index():
    """Dashboard home page."""
    if 'token' not in session:
        return redirect(url_for('login'))

    # Get dashboard data
    dashboard_data, status_code = make_api_request('/admin/dashboard', token=session['token'])

    if status_code != 200:
        flash('Failed to load dashboard data', 'error')
        dashboard_data = {'data': {'overview': {}}}

    return render_template('dashboard.html', dashboard=dashboard_data.get('data', {}))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login page."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Authenticate with API
        auth_data, status_code = make_api_request('/auth/login', 'POST', {
            'login': email,
            'password': password
        })

        if status_code == 200 and auth_data.get('success'):
            token = auth_data['data']['access_token']

            # Check if user is admin
            permissions, perm_status = make_api_request('/auth/permissions', token=token)

            if perm_status == 200 and permissions.get('data', {}).get('is_admin'):
                session['token'] = token
                session['user'] = auth_data['data']['user']
                flash('Login successful', 'success')
                return redirect(url_for('index'))
            else:
                flash('Admin access required', 'error')
        else:
            flash('Invalid credentials', 'error')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout and clear session."""
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


@app.route('/users')
def users():
    """Users management page."""
    if 'token' not in session:
        return redirect(url_for('login'))

    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    plan = request.args.get('plan', '')
    status = request.args.get('status', '')

    params = {'page': page, 'per_page': 20}
    if search:
        params['search'] = search
    if plan:
        params['plan'] = plan
    if status:
        params['status'] = status

    users_data, status_code = make_api_request('/admin/users', data=params, token=session['token'])

    if status_code != 200:
        flash('Failed to load users data', 'error')
        users_data = {'data': {'items': [], 'pagination': {}}}

    return render_template('users.html',
                         users_data=users_data.get('data', {}),
                         current_filters={'search': search, 'plan': plan, 'status': status})


@app.route('/users/<user_id>')
def user_detail(user_id):
    """User detail page."""
    if 'token' not in session:
        return redirect(url_for('login'))

    user_data, status_code = make_api_request(f'/admin/users/{user_id}', token=session['token'])

    if status_code != 200:
        flash('User not found', 'error')
        return redirect(url_for('users'))

    return render_template('user_detail.html', user=user_data.get('data', {}))


@app.route('/users/<user_id>/deactivate', methods=['POST'])
def deactivate_user(user_id):
    """Deactivate a user."""
    if 'token' not in session:
        return redirect(url_for('login'))

    result, status_code = make_api_request(f'/admin/users/{user_id}/deactivate', 'POST', token=session['token'])

    if status_code == 200:
        flash('User deactivated successfully', 'success')
    else:
        flash('Failed to deactivate user', 'error')

    return redirect(url_for('user_detail', user_id=user_id))


@app.route('/users/<user_id>/reactivate', methods=['POST'])
def reactivate_user(user_id):
    """Reactivate a user."""
    if 'token' not in session:
        return redirect(url_for('login'))

    result, status_code = make_api_request(f'/admin/users/{user_id}/reactivate', 'POST', token=session['token'])

    if status_code == 200:
        flash('User reactivated successfully', 'success')
    else:
        flash('Failed to reactivate user', 'error')

    return redirect(url_for('user_detail', user_id=user_id))


@app.route('/billing')
def billing():
    """Billing overview page."""
    if 'token' not in session:
        return redirect(url_for('login'))

    # Get date range from query parameters
    start_date = request.args.get('start_date', (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    end_date = request.args.get('end_date', datetime.now().strftime('%Y-%m-%d'))

    params = {'start_date': start_date, 'end_date': end_date}

    billing_data, status_code = make_api_request('/admin/billing/overview', data=params, token=session['token'])

    if status_code != 200:
        flash('Failed to load billing data', 'error')
        billing_data = {'data': {}}

    return render_template('billing.html',
                         billing=billing_data.get('data', {}),
                         start_date=start_date,
                         end_date=end_date)


@app.route('/usage')
def usage():
    """Usage analytics page."""
    if 'token' not in session:
        return redirect(url_for('login'))

    # Get date range from query parameters
    start_date = request.args.get('start_date', (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    end_date = request.args.get('end_date', datetime.now().strftime('%Y-%m-%d'))

    params = {'start_date': start_date, 'end_date': end_date}

    usage_data, status_code = make_api_request('/admin/usage/analytics', data=params, token=session['token'])

    if status_code != 200:
        flash('Failed to load usage data', 'error')
        usage_data = {'data': {}}

    return render_template('usage.html',
                         usage=usage_data.get('data', {}),
                         start_date=start_date,
                         end_date=end_date)


@app.route('/system')
def system():
    """System health and metrics page."""
    if 'token' not in session:
        return redirect(url_for('login'))

    health_data, status_code = make_api_request('/admin/system/health', token=session['token'])

    if status_code != 200:
        flash('Failed to load system data', 'error')
        health_data = {'data': {}}

    return render_template('system.html', health=health_data.get('data', {}))


@app.route('/reports')
def reports():
    """Reports page."""
    if 'token' not in session:
        return redirect(url_for('login'))

    return render_template('reports.html')


@app.route('/api/dashboard/refresh')
def refresh_dashboard():
    """API endpoint to refresh dashboard data."""
    if 'token' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    dashboard_data, status_code = make_api_request('/admin/dashboard', token=session['token'])

    if status_code == 200:
        return jsonify(dashboard_data)
    else:
        return jsonify({'error': 'Failed to refresh data'}), status_code


# Template filters
@app.template_filter('currency')
def currency_filter(amount):
    """Format amount as currency."""
    return f"${amount:,.2f}"


@app.template_filter('number')
def number_filter(value):
    """Format number with commas."""
    return f"{value:,}"


@app.template_filter('percentage')
def percentage_filter(value):
    """Format value as percentage."""
    return f"{value:.1f}%"


@app.template_filter('datetime')
def datetime_filter(value):
    """Format datetime string."""
    if isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return value
    return value


@app.template_filter('date')
def date_filter(value):
    """Format date string."""
    if isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d')
        except:
            return value
    return value


@app.template_filter('status_badge')
def status_badge_filter(status):
    """Convert status to Bootstrap badge class."""
    status_classes = {
        'active': 'badge-success',
        'inactive': 'badge-secondary',
        'pending': 'badge-warning',
        'paid': 'badge-success',
        'overdue': 'badge-danger',
        'cancelled': 'badge-secondary',
        'healthy': 'badge-success',
        'degraded': 'badge-warning',
        'unhealthy': 'badge-danger'
    }
    return status_classes.get(status.lower(), 'badge-secondary')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=DASHBOARD_PORT)