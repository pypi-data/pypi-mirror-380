"""
Database handler for Python Event Journal.

This module provides database connection and operation functionality
for the event journal without requiring Django.
"""

import psycopg2
import psycopg2.extras
from datetime import datetime
from typing import Optional, Dict, Any, List, Tuple, Union
import json
import uuid


class DatabaseHandler:
    """
    Database handler for PostgreSQL operations.
    
    This class manages database connections and provides methods for
    CRUD operations on the event journal table.
    """
    
    def __init__(self, 
                 host: str = 'aws-1-ap-southeast-1.pooler.supabase.com',
                 port: int = 6543,
                 database: str = 'postgres',
                 user: str = 'postgres.xelettnjdfbmhiealved',
                 password: str = 'celJ1N0mnz0gkrLm',
                 sslmode: str = 'require'):
        """
        Initialize database handler.
        
        Args:
            host: Database host
            port: Database port
            database: Database name
            user: Database username
            password: Database password
            sslmode: SSL mode for connection
        """
        self.connection_params = {
            'host': host,
            'port': port,
            'database': database,
            'user': user,
            'password': password,
            'sslmode': sslmode
        }
        self._connection = None
    
    def connect(self) -> psycopg2.extensions.connection:
        """
        Establish database connection.
        
        Returns:
            psycopg2 connection object
            
        Raises:
            psycopg2.Error: If connection fails
        """
        if self._connection is None or self._connection.closed:
            self._connection = psycopg2.connect(**self.connection_params)
        return self._connection
    
    def close(self):
        """Close database connection."""
        if self._connection and not self._connection.closed:
            self._connection.close()
            self._connection = None
    
    def test_connection(self) -> bool:
        """
        Test database connection.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            conn = self.connect()
            with conn.cursor() as cursor:
                cursor.execute("SELECT version();")
                version = cursor.fetchone()[0]
                print(f"✅ Connected to PostgreSQL: {version}")
                return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
    
    def check_table_exists(self, table_name: str = 'event_journal') -> bool:
        """
        Check if the event journal table exists.
        
        Args:
            table_name: Name of the table to check
            
        Returns:
            bool: True if table exists, False otherwise
        """
        try:
            conn = self.connect()
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = %s
                    );
                """, (table_name,))
                table_exists = cursor.fetchone()[0]
            
            if table_exists:
                print("✅ EventJournal table found in database.")
                return True
            else:
                print("❌ EventJournal table not found in database.")
                print("Please ensure the table exists before using the library.")
                return False
                
        except Exception as e:
            print(f"❌ Error checking table: {e}")
            return False
    
    def create_event(self, 
                    event_type: str,
                    user_id: Optional[int] = None,
                    event_info: Optional[Dict[str, Any]] = None,
                    ip_address: Optional[str] = None,
                    user_agent: str = '',
                    timestamp: Optional[datetime] = None) -> str:
        """
        Create a new event journal entry.
        
        Args:
            event_type: Type of event being logged
            user_id: ID of the user associated with this event
            event_info: Additional event information as dictionary
            ip_address: Client IP address
            user_agent: Client user agent string
            timestamp: Event timestamp (defaults to now)
            
        Returns:
            int: ID of the created event
            
        Raises:
            psycopg2.Error: If database operation fails
        """
        if event_info is None:
            event_info = {}
        
        if timestamp is None:
            timestamp = datetime.utcnow()
        
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO event_journal 
                (event_type, user_id, event_info, ip_address, user_agent, timestamp, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id;
            """, (
                event_type,
                user_id,
                json.dumps(event_info),
                ip_address,
                user_agent,
                timestamp,
                datetime.utcnow()
            ))
            event_id = cursor.fetchone()[0]
            conn.commit()
            return event_id
    
    def get_event(self, event_id: int) -> Optional[Dict[str, Any]]:
        """
        Get an event by ID.
        
        Args:
            event_id: ID of the event to retrieve
            
        Returns:
            dict: Event data or None if not found
        """
        try:
            conn = self.connect()
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT * FROM event_journal 
                    WHERE id = %s;
                """, (event_id,))
                row = cursor.fetchone()
                
                if row:
                    # Convert to regular dict and parse JSON
                    event_data = dict(row)
                    if event_data['event_info']:
                        event_data['event_info'] = json.loads(event_data['event_info'])
                    return event_data
                return None
        except Exception as e:
            print(f"❌ Error retrieving event: {e}")
            return None
    
    def get_events(self, 
                  event_type: Optional[str] = None,
                  user_id: Optional[int] = None,
                  limit: int = 100,
                  offset: int = 0,
                  order_by: str = 'timestamp DESC') -> List[Dict[str, Any]]:
        """
        Get events with optional filtering.
        
        Args:
            event_type: Filter by event type
            user_id: Filter by user ID
            limit: Maximum number of events to return
            offset: Number of events to skip
            order_by: Order by clause
            
        Returns:
            list: List of event dictionaries
        """
        try:
            conn = self.connect()
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                where_conditions = []
                params = []
                
                if event_type:
                    where_conditions.append("event_type = %s")
                    params.append(event_type)
                
                if user_id is not None:
                    where_conditions.append("user_id = %s")
                    params.append(user_id)
                
                where_clause = ""
                if where_conditions:
                    where_clause = "WHERE " + " AND ".join(where_conditions)
                
                query = f"""
                    SELECT * FROM event_journal 
                    {where_clause}
                    ORDER BY {order_by}
                    LIMIT %s OFFSET %s;
                """
                params.extend([limit, offset])
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                events = []
                for row in rows:
                    event_data = dict(row)
                    if event_data['event_info']:
                        event_data['event_info'] = json.loads(event_data['event_info'])
                    events.append(event_data)
                
                return events
        except Exception as e:
            print(f"❌ Error retrieving events: {e}")
            return []
    
    def count_events(self, 
                    event_type: Optional[str] = None,
                    user_id: Optional[int] = None) -> int:
        """
        Count events with optional filtering.
        
        Args:
            event_type: Filter by event type
            user_id: Filter by user ID
            
        Returns:
            int: Number of events matching the criteria
        """
        try:
            conn = self.connect()
            with conn.cursor() as cursor:
                where_conditions = []
                params = []
                
                if event_type:
                    where_conditions.append("event_type = %s")
                    params.append(event_type)
                
                if user_id is not None:
                    where_conditions.append("user_id = %s")
                    params.append(user_id)
                
                where_clause = ""
                if where_conditions:
                    where_clause = "WHERE " + " AND ".join(where_conditions)
                
                query = f"SELECT COUNT(*) FROM event_journal {where_clause};"
                cursor.execute(query, params)
                count = cursor.fetchone()[0]
                return count
        except Exception as e:
            print(f"❌ Error counting events: {e}")
            return 0
    
    def delete_event(self, event_id: int) -> bool:
        """
        Delete an event by ID.
        
        Args:
            event_id: ID of the event to delete
            
        Returns:
            bool: True if deleted successfully, False otherwise
        """
        try:
            conn = self.connect()
            with conn.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM event_journal 
                    WHERE id = %s;
                """, (event_id,))
                deleted_count = cursor.rowcount
                conn.commit()
                return deleted_count > 0
        except Exception as e:
            print(f"❌ Error deleting event: {e}")
            return False
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
