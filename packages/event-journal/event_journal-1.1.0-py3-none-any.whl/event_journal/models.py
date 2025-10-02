"""
Event Journal models for Python Event Journal.

This module provides the EventJournal model and related functionality
for logging events to PostgreSQL database.
"""

from datetime import datetime
from typing import Optional, Dict, Any
import json


class EventJournal:
    """
    Model for storing event logs in PostgreSQL database.
    
    This model stores various types of events with associated metadata
    including user information, event details, IP address, and user agent.
    """
    
    def __init__(self, 
                 event_type: str,
                 user_id: Optional[int] = None,
                 event_info: Optional[Dict[str, Any]] = None,
                 ip_address: Optional[str] = None,
                 user_agent: str = '',
                 timestamp: Optional[datetime] = None,
                 event_id: Optional[int] = None,
                 created_at: Optional[datetime] = None):
        """
        Initialize EventJournal instance.
        
        Args:
            event_type: Type of event being logged
            user_id: ID of the user associated with this event
            event_info: Additional event information
            ip_address: Client IP address
            user_agent: Client user agent string
            timestamp: When the event occurred
            event_id: Database ID of the event (for existing events)
            created_at: When this event log entry was created
        """
        self.id = event_id
        self.event_type = event_type
        self.user_id = user_id
        self.event_info = event_info or {}
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.timestamp = timestamp or datetime.utcnow()
        self.created_at = created_at or datetime.utcnow()
    
    def __str__(self):
        """String representation of the event."""
        user_info = f"User ID: {self.user_id}" if self.user_id else "System"
        return f"{self.event_type} - {user_info} - {self.timestamp}"
    
    def __repr__(self):
        """Detailed string representation of the event."""
        return (f"EventJournal(id={self.id}, event_type='{self.event_type}', "
                f"user_id={self.user_id}, timestamp={self.timestamp})")
    
    def get_event_info_display(self) -> str:
        """
        Return a formatted string representation of event_info.
        
        Returns:
            str: Formatted JSON string or fallback representation
        """
        if not self.event_info:
            return "No additional information"
        
        try:
            return json.dumps(self.event_info, indent=2, default=str)
        except (TypeError, ValueError):
            return str(self.event_info)
    
    def get_user_display(self) -> str:
        """
        Return a formatted string representation of the user.
        
        Returns:
            str: User information or "System"
        """
        if not self.user_id:
            return "System"
        
        return f"User ID: {self.user_id}"
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the event to a dictionary.
        
        Returns:
            dict: Event data as dictionary
        """
        return {
            'id': self.id,
            'event_type': self.event_type,
            'user_id': self.user_id,
            'event_info': self.event_info,
            'ip_address': self.ip_address,
            'user_agent': self.user_agent,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EventJournal':
        """
        Create EventJournal instance from dictionary.
        
        Args:
            data: Dictionary containing event data
            
        Returns:
            EventJournal: New instance
        """
        # Parse datetime strings if present
        timestamp = data.get('timestamp')
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        
        created_at = data.get('created_at')
        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        
        return cls(
            event_id=data.get('id'),
            event_type=data['event_type'],
            user_id=data.get('user_id'),
            event_info=data.get('event_info', {}),
            ip_address=data.get('ip_address'),
            user_agent=data.get('user_agent', ''),
            timestamp=timestamp,
            created_at=created_at
        )
    
    @classmethod
    def log_event(cls,
                  event_type: str,
                  user_id: Optional[int] = None,
                  event_info: Optional[Dict[str, Any]] = None,
                  ip_address: Optional[str] = None,
                  user_agent: str = '',
                  timestamp: Optional[datetime] = None,
                  db_handler=None) -> 'EventJournal':
        """
        Log an event to the database.
        
        Args:
            event_type: Type of event being logged
            user_id: ID of the user associated with this event
            event_info: Additional event information
            ip_address: Client IP address
            user_agent: Client user agent string
            timestamp: Event timestamp (defaults to now)
            db_handler: DatabaseHandler instance (if None, uses default)
        
        Returns:
            EventJournal: The created EventJournal instance
        
        Example:
            EventJournal.log_event(
                event_type='duplicate_upload_attempt',
                user_id=user.id,
                event_info={
                    'file_id': existing_file.id,
                    'filename': existing_file.original_filename,
                    'file_type': existing_file.file_type,
                    'size': existing_file.size,
                    'checksum': existing_file.checksum,
                    'is_new_file': False,
                    'is_deduplication': False,
                    'reference_count': existing_file.reference_count,
                    'user_relationship_type': 'owner' if file_user.is_owner else 'reference'
                },
                ip_address='192.168.1.1',
                user_agent='Mozilla/5.0...'
            )
        """
        if db_handler is None:
            from .database import DatabaseHandler
            db_handler = DatabaseHandler()
        
        # Create the event in the database
        event_id = db_handler.create_event(
            event_type=event_type,
            user_id=user_id,
            event_info=event_info,
            ip_address=ip_address,
            user_agent=user_agent,
            timestamp=timestamp
        )
        
        # Create and return the EventJournal instance
        return cls(
            event_id=event_id,
            event_type=event_type,
            user_id=user_id,
            event_info=event_info or {},
            ip_address=ip_address,
            user_agent=user_agent,
            timestamp=timestamp or datetime.utcnow(),
            created_at=datetime.utcnow()
        )
