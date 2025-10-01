"""
BioQL Natural Language Parser Module

This module provides natural language parsing capabilities for BioQL,
including pattern-based and LLM-powered parsers.
"""

from .llm_parser import (
    HybridParser,
    LLMConfig,
    LLMParser,
    LLMParsingError,
    parse_natural_language,
)
from .nl_parser import (
    MoleculeExtractor,
    NaturalLanguageParser,
    ParameterExtractor,
    ParseError,
    PatternMatcher,
)

__all__ = [
    # Core parsing classes
    "NaturalLanguageParser",
    "PatternMatcher",
    "MoleculeExtractor",
    "ParameterExtractor",
    "ParseError",
    # LLM-powered parsing
    "LLMConfig",
    "LLMParser",
    "LLMParsingError",
    "HybridParser",
    "parse_natural_language",
]