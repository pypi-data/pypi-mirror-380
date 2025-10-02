"""
Python Event Journal - A simple Python library for logging events to PostgreSQL database.

This library provides a simple way to log events to a PostgreSQL database without
requiring Django or any other web framework.
"""

from .models import EventJournal
from .database import DatabaseHandler
from .utils import get_client_ip, get_user_agent, get_request_info
from .standalone import log_event, test_connection, check_table_exists

__version__ = "1.1.0"
__author__ = "Amol Saini"
__email__ = "amol.saini567@gmail.com"

__all__ = [
    'EventJournal',
    'DatabaseHandler', 
    'log_event',
    'test_connection',
    'check_table_exists',
    'get_client_ip',
    'get_user_agent',
    'get_request_info'
]
