"""
Standalone Python Event Journal.

This module allows you to use the Python Event Journal without any web framework.
It provides simple functions for logging events to PostgreSQL database.
"""

from datetime import datetime
from typing import Optional, Dict, Any
from .database import DatabaseHandler
from .models import EventJournal
from .utils import get_client_ip, get_user_agent, get_request_info


# Global database handler instance
_db_handler = None


def get_db_handler() -> DatabaseHandler:
    """
    Get the global database handler instance.
    
    Returns:
        DatabaseHandler: Global database handler
    """
    global _db_handler
    if _db_handler is None:
        _db_handler = DatabaseHandler()
    return _db_handler


def log_event(event_type: str,
              user_id: Optional[int] = None,
              event_info: Optional[Dict[str, Any]] = None,
              ip_address: Optional[str] = None,
              user_agent: str = '',
              timestamp: Optional[datetime] = None) -> EventJournal:
    """
    Standalone function to log an event.
    
    This function provides a simple interface for logging events to the database.
    It automatically manages database connections.
    
    Args:
        event_type (str): Type of event being logged
        user_id (int, optional): ID of the user associated with this event
        event_info (dict, optional): Additional event information
        ip_address (str, optional): Client IP address
        user_agent (str, optional): Client user agent string
        timestamp (datetime, optional): Event timestamp (defaults to now)
    
    Returns:
        EventJournal: The created EventJournal instance
    
    Example:
        from python_event_journal import log_event
        
        # Log an event
        event_log = log_event(
            event_type='user_event',
            event_info={'event': 'login', 'method': 'email'},
            ip_address='192.168.1.1',
            user_agent='Mozilla/5.0...'
        )
    """
    db_handler = get_db_handler()
    
    # Log the event
    return EventJournal.log_event(
        event_type=event_type,
        user_id=user_id,
        event_info=event_info,
        ip_address=ip_address,
        user_agent=user_agent,
        timestamp=timestamp,
        db_handler=db_handler
    )


def test_connection() -> bool:
    """
    Test the database connection.
    
    Returns:
        bool: True if connection successful, False otherwise
    """
    db_handler = get_db_handler()
    return db_handler.test_connection()


def check_table_exists() -> bool:
    """
    Check if EventJournal table exists in the database.
    
    Returns:
        bool: True if table exists, False otherwise
    """
    db_handler = get_db_handler()
    return db_handler.check_table_exists()


def get_events(event_type: Optional[str] = None,
               user_id: Optional[int] = None,
               limit: int = 100,
               offset: int = 0) -> list:
    """
    Get events with optional filtering.
    
    Args:
        event_type: Filter by event type
        user_id: Filter by user ID
        limit: Maximum number of events to return
        offset: Number of events to skip
        
    Returns:
        list: List of event dictionaries
    """
    db_handler = get_db_handler()
    return db_handler.get_events(
        event_type=event_type,
        user_id=user_id,
        limit=limit,
        offset=offset
    )


def get_event(event_id: int) -> Optional[Dict[str, Any]]:
    """
    Get an event by ID.
    
    Args:
        event_id: ID of the event to retrieve
        
    Returns:
        dict: Event data or None if not found
    """
    db_handler = get_db_handler()
    return db_handler.get_event(event_id)


def count_events(event_type: Optional[str] = None,
                user_id: Optional[int] = None) -> int:
    """
    Count events with optional filtering.
    
    Args:
        event_type: Filter by event type
        user_id: Filter by user ID
        
    Returns:
        int: Number of events matching the criteria
    """
    db_handler = get_db_handler()
    return db_handler.count_events(event_type=event_type, user_id=user_id)


def delete_event(event_id: int) -> bool:
    """
    Delete an event by ID.
    
    Args:
        event_id: ID of the event to delete
        
    Returns:
        bool: True if deleted successfully, False otherwise
    """
    db_handler = get_db_handler()
    return db_handler.delete_event(event_id)


def close_connection():
    """
    Close the database connection.
    
    This is useful for cleanup when your application is shutting down.
    """
    global _db_handler
    if _db_handler:
        _db_handler.close()
        _db_handler = None


# Convenience functions for common use cases
def log_user_login(user_id: int, 
                  login_method: str = 'email',
                  ip_address: Optional[str] = None,
                  user_agent: str = '',
                  **kwargs) -> EventJournal:
    """
    Log a user login event.
    
    Args:
        user_id: ID of the user logging in
        login_method: Method used for login (email, social, etc.)
        ip_address: Client IP address
        user_agent: Client user agent string
        **kwargs: Additional event information
        
    Returns:
        EventJournal: The created event
    """
    event_info = {
        'login_method': login_method,
        'success': True,
        **kwargs
    }
    
    return log_event(
        event_type='user_login',
        user_id=user_id,
        event_info=event_info,
        ip_address=ip_address,
        user_agent=user_agent
    )


def log_user_logout(user_id: int,
                   ip_address: Optional[str] = None,
                   user_agent: str = '',
                   **kwargs) -> EventJournal:
    """
    Log a user logout event.
    
    Args:
        user_id: ID of the user logging out
        ip_address: Client IP address
        user_agent: Client user agent string
        **kwargs: Additional event information
        
    Returns:
        EventJournal: The created event
    """
    event_info = {
        'success': True,
        **kwargs
    }
    
    return log_event(
        event_type='user_logout',
        user_id=user_id,
        event_info=event_info,
        ip_address=ip_address,
        user_agent=user_agent
    )


def log_file_upload(user_id: int,
                   file_id: str,
                   filename: str,
                   file_type: str,
                   file_size: int,
                   ip_address: Optional[str] = None,
                   user_agent: str = '',
                   **kwargs) -> EventJournal:
    """
    Log a file upload event.
    
    Args:
        user_id: ID of the user uploading the file
        file_id: Unique identifier for the file
        filename: Original filename
        file_type: MIME type of the file
        file_size: Size of the file in bytes
        ip_address: Client IP address
        user_agent: Client user agent string
        **kwargs: Additional event information
        
    Returns:
        EventJournal: The created event
    """
    event_info = {
        'file_id': file_id,
        'filename': filename,
        'file_type': file_type,
        'size': file_size,
        'upload_method': 'web_interface',
        **kwargs
    }
    
    return log_event(
        event_type='file_upload',
        user_id=user_id,
        event_info=event_info,
        ip_address=ip_address,
        user_agent=user_agent
    )


def log_api_request(endpoint: str,
                   method: str,
                   status_code: int,
                   user_id: Optional[int] = None,
                   response_time_ms: Optional[int] = None,
                   ip_address: Optional[str] = None,
                   user_agent: str = '',
                   **kwargs) -> EventJournal:
    """
    Log an API request event.
    
    Args:
        endpoint: API endpoint that was called
        method: HTTP method (GET, POST, etc.)
        status_code: HTTP status code returned
        user_id: ID of the user making the request
        response_time_ms: Response time in milliseconds
        ip_address: Client IP address
        user_agent: Client user agent string
        **kwargs: Additional event information
        
    Returns:
        EventJournal: The created event
    """
    event_info = {
        'endpoint': endpoint,
        'method': method,
        'status_code': status_code,
        'response_time_ms': response_time_ms,
        **kwargs
    }
    
    return log_event(
        event_type='api_request',
        user_id=user_id,
        event_info=event_info,
        ip_address=ip_address,
        user_agent=user_agent
    )
