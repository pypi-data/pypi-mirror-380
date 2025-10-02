"""
Utility functions for Python Event Journal.

This module provides utility functions for extracting request information
and other common operations.
"""

from typing import Optional, Dict, Any
import json


def get_client_ip(request_headers: Optional[Dict[str, str]] = None) -> Optional[str]:
    """
    Extract the client IP address from request headers.
    
    This function checks various headers to determine the real client IP,
    taking into account proxies and load balancers.
    
    Args:
        request_headers: Dictionary of request headers (e.g., from Flask request.headers)
        
    Returns:
        str: Client IP address or None if not found
        
    Example:
        # With Flask
        ip_address = get_client_ip(dict(request.headers))
        
        # With custom headers dict
        headers = {'X-Forwarded-For': '192.168.1.1, 10.0.0.1'}
        ip_address = get_client_ip(headers)
    """
    if not request_headers:
        return None
    
    # Check for forwarded IP first (common with proxies/load balancers)
    x_forwarded_for = request_headers.get('X-Forwarded-For')
    if x_forwarded_for:
        # X-Forwarded-For can contain multiple IPs, take the first one
        ip = x_forwarded_for.split(',')[0].strip()
        return ip
    
    # Check for real IP header
    x_real_ip = request_headers.get('X-Real-IP')
    if x_real_ip:
        return x_real_ip.strip()
    
    # Check for client IP header
    x_client_ip = request_headers.get('X-Client-IP')
    if x_client_ip:
        return x_client_ip.strip()
    
    # Check for CF-Connecting-IP (Cloudflare)
    cf_connecting_ip = request_headers.get('CF-Connecting-IP')
    if cf_connecting_ip:
        return cf_connecting_ip.strip()
    
    # Fall back to remote address
    remote_addr = request_headers.get('Remote-Addr')
    if remote_addr:
        return remote_addr.strip()
    
    return None


def get_user_agent(request_headers: Optional[Dict[str, str]] = None) -> str:
    """
    Extract the user agent string from request headers.
    
    Args:
        request_headers: Dictionary of request headers
        
    Returns:
        str: User agent string or empty string if not found
        
    Example:
        # With Flask
        user_agent = get_user_agent(dict(request.headers))
        
        # With custom headers dict
        headers = {'User-Agent': 'Mozilla/5.0...'}
        user_agent = get_user_agent(headers)
    """
    if not request_headers:
        return ''
    
    return request_headers.get('User-Agent', '')


def get_request_info(request_headers: Optional[Dict[str, str]] = None,
                    request_method: Optional[str] = None,
                    request_path: Optional[str] = None,
                    query_string: Optional[str] = None) -> Dict[str, Any]:
    """
    Extract comprehensive request information.
    
    Args:
        request_headers: Dictionary of request headers
        request_method: HTTP method (GET, POST, etc.)
        request_path: Request path/URL
        query_string: Query string parameters
        
    Returns:
        dict: Dictionary containing IP address, user agent, and other request info
        
    Example:
        # With Flask
        request_info = get_request_info(
            request_headers=dict(request.headers),
            request_method=request.method,
            request_path=request.path,
            query_string=request.query_string.decode()
        )
        # Returns: {
        #     'ip_address': '192.168.1.1',
        #     'user_agent': 'Mozilla/5.0...',
        #     'method': 'POST',
        #     'path': '/api/upload/',
        #     'query_string': 'param=value'
        # }
    """
    if not request_headers:
        return {}
    
    return {
        'ip_address': get_client_ip(request_headers),
        'user_agent': get_user_agent(request_headers),
        'method': request_method,
        'path': request_path,
        'query_string': query_string or '',
        'content_type': request_headers.get('Content-Type', ''),
        'referer': request_headers.get('Referer', ''),
    }


def format_event_info(event_info: Dict[str, Any]) -> str:
    """
    Format event info dictionary as a readable string.
    
    Args:
        event_info: Dictionary containing event information
        
    Returns:
        str: Formatted string representation
    """
    if not event_info:
        return "No additional information"
    
    try:
        return json.dumps(event_info, indent=2, default=str)
    except (TypeError, ValueError):
        return str(event_info)


def validate_event_type(event_type: str) -> bool:
    """
    Validate event type string.
    
    Args:
        event_type: Event type to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(event_type, str):
        return False
    
    if not event_type.strip():
        return False
    
    if len(event_type) > 100:
        return False
    
    # Check for valid characters (alphanumeric, underscore, hyphen)
    import re
    if not re.match(r'^[a-zA-Z0-9_-]+$', event_type):
        return False
    
    return True


def validate_ip_address(ip_address: Optional[str]) -> bool:
    """
    Validate IP address format.
    
    Args:
        ip_address: IP address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if ip_address is None:
        return True
    
    if not isinstance(ip_address, str):
        return False
    
    import re
    # IPv4 pattern
    ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    # IPv6 pattern (simplified)
    ipv6_pattern = r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    return bool(re.match(ipv4_pattern, ip_address) or re.match(ipv6_pattern, ip_address))


def sanitize_user_agent(user_agent: str) -> str:
    """
    Sanitize user agent string to prevent injection attacks.
    
    Args:
        user_agent: Raw user agent string
        
    Returns:
        str: Sanitized user agent string
    """
    if not user_agent:
        return ''
    
    # Remove or replace potentially dangerous characters
    import re
    # Keep only printable ASCII characters and common Unicode
    sanitized = re.sub(r'[^\x20-\x7E\u00A0-\uFFFF]', '', user_agent)
    
    # Limit length to prevent abuse
    return sanitized[:500]
