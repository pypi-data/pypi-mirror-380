from typing import Optional, Dict, Any, List
import requests
from loguru import logger
from datetime import datetime, timedelta
import jwt
from getpass import getpass

class AuthError(Exception):
    """Base exception for authentication errors"""
    pass

class Client:
    """
    A client for interacting with the Mantle API.
    
    Args:
        base_url: Base URL of the Mantle server
        email: User email for authentication
        password: User password for authentication
        auto_refresh: Whether to automatically refresh tokens before expiry
    """
    
    def __init__(
        self, 
        base_url: str, 
        email: Optional[str] = None,
        password: Optional[str] = None,
        auto_refresh: bool = True
    ):
        self.base_url = base_url.rstrip('/')
        self._email = email
        self._password = password
        self._token: Optional[str] = None
        self._token_expiry: Optional[datetime] = None
        self.auto_refresh = auto_refresh
        
        # Login if credentials provided
        if email and password:
            self.login(email, password)

    def _get_headers(self) -> Dict[str, str]:
        """Get headers with current authentication token"""
        if not self._token:
            raise AuthError("Not authenticated. Please login first.")
            
        # Check if token needs refresh
        if self.auto_refresh and self._should_refresh_token():
            self.login(self._email, self._password)
            
        return {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }
    
    def _should_refresh_token(self) -> bool:
        """Check if token should be refreshed (within 5 minutes of expiry)"""
        if not self._token_expiry:
            return False
        return datetime.now() + timedelta(minutes=5) >= self._token_expiry
    
    def _extract_token_expiry(self, token: str) -> datetime:
        """Extract token expiry time from JWT"""
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            return datetime.fromtimestamp(decoded['exp'])
        except Exception as e:
            logger.warning(f"Failed to decode token expiry: {e}")
            # Default to 1 hour from now if we can't decode
            return datetime.now() + timedelta(hours=1)

    def login(self, email: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """
        Login to the Mantle server.
        
        Args:
            email: User email (optional if provided at initialization)
            password: User password (optional if provided at initialization)
            
        Returns:
            Dict containing login response
        """
        email = email or self._email
        password = password or self._password
        
        if not email or not password:
            raise AuthError("Email and password required")
            
        response = requests.post(
            f"{self.base_url}/auth/jwt/login",
            data={"username": email, "password": password}
        )
        
        if response.status_code == 200:
            data = response.json()
            self._token = data['access_token']
            self._token_expiry = self._extract_token_expiry(self._token)
            self._email = email
            self._password = password
            return data
        else:
            raise AuthError(f"Login failed: {response.text}")
    
    def register(self, email: str, password: str) -> Dict[str, Any]:
        """
        Register a new user.
        
        Args:
            email: User email
            password: User password
            
        Returns:
            Dict containing registration response
        """
        response = requests.post(
            f"{self.base_url}/auth/register",
            json={"email": email, "password": password}
        )
        
        if response.status_code == 201:
            return response.json()
        else:
            raise AuthError(f"Registration failed: {response.text}")

    def request_verify_token(self, email: Optional[str] = None) -> requests.Response:
        """Request verification token"""
        email = email or self._email
        if not email:
            raise AuthError("Email required")
            
        url = f"{self.base_url}/auth/request-verify-token"
        response = requests.post(url, json={"email": email})
        
        if response.status_code == 202:
            print("Verification token has been sent to your email.")
        else:
            print("Failed to send verification token:", response.json())
        return response

    def verify_email(self, token: str) -> requests.Response:
        """Verify email with token"""
        url = f"{self.base_url}/auth/verify"
        response = requests.post(url, json={"token": token})
        
        if response.status_code == 200:
            print("Email verified successfully!")
        else:
            print("Email verification failed:", response.json())
        return response

    def request_password_reset(self, email: Optional[str] = None) -> requests.Response:
        """Request password reset token"""
        email = email or self._email
        if not email:
            raise AuthError("Email required")
            
        url = f"{self.base_url}/auth/forgot-password"
        response = requests.post(url, json={"email": email})
        
        if response.status_code == 202:
            print("Password reset token has been sent to your email.")
        else:
            print("Failed to send password reset token:", response.json())
        return response

    def reset_password(self, token: str) -> requests.Response:
        """Reset password using token"""
        url = f"{self.base_url}/auth/reset-password"
        new_password = getpass("Enter your new password (hidden): ")
        confirm_password = getpass("Confirm your new password (hidden): ")
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            return None
        
        response = requests.post(url, json={"token": token, "password": new_password})
        
        if response.status_code == 200:
            print("Password reset successfully!")
        else:
            print("Password reset failed:", response.json())
        return response
    
    def get_current_user(self) -> Dict[str, Any]:
        """
        Get current user details.
        
        Returns:
            Dict containing user details
        """
        response = requests.get(
            f"{self.base_url}/users/me",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to get user details: {response.text}")
    
    def list_users(self) -> List[Dict[str, Any]]:
        """
        List all users (requires admin privileges).
        
        Returns:
            List of user details
        """
        response = requests.get(
            f"{self.base_url}/users",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to list users: {response.text}")
    
    def update_user(self, user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update user details.
        
        Args:
            user_id: ID of user to update
            data: Dict containing fields to update
            
        Returns:
            Dict containing updated user details
        """
        response = requests.patch(
            f"{self.base_url}/users/{user_id}",
            headers=self._get_headers(),
            json=data
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to update user: {response.text}")
    
    def delete_user(self, user_id: str) -> bool:
        """
        Delete a user.
        
        Args:
            user_id: ID of user to delete
            
        Returns:
            True if successful
        """
        response = requests.delete(
            f"{self.base_url}/users/{user_id}",
            headers=self._get_headers()
        )
        
        if response.status_code == 204:
            return True
        else:
            raise AuthError(f"Failed to delete user: {response.text}")
        
    def list_databases(self) -> List[str]:
        """
        List all attached databases.
        
        Returns:
            List of database names
            
        Raises:
            AuthError: If not authenticated
            HTTPError: If request fails
        """
        response = requests.get(
            f"{self.base_url}/db/list",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to list databases: {response.text}")
        
    def attach_database(self, path: str, name: str) -> Dict[str, str]:
        """
        Attach a database to the server.
        
        Args:
            path: Path to the database file
            name: Name to assign to the database
            
        Returns:
            Dict containing success message
            
        Raises:
            AuthError: If not authenticated or insufficient permissions
            HTTPError: If attachment fails
        """
        response = requests.post(
            f"{self.base_url}/db/attach",
            headers=self._get_headers(),
            json={
                "path": path,
                "name": name
            }
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to attach database: {response.text}")
            
    def detach_database(self, name: str) -> Dict[str, str]:
        """
        Detach a database from the server.
        
        Args:
            name: Name of the database to detach
            
        Returns:
            Dict containing success message
            
        Raises:
            AuthError: If not authenticated or insufficient permissions
            HTTPError: If detachment fails
        """
        response = requests.delete(
            f"{self.base_url}/db/{name}",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to detach database: {response.text}")
        
    def execute_query(self, database: str, query: str) -> List[Dict[str, Any]]:
        """
        Execute a SQL query on an attached database.
        
        Args:
            database: Name of the attached database
            query: SQL query to execute
            
        Returns:
            List of dictionaries containing query results
            
        Raises:
            AuthError: If not authenticated
            HTTPError: If query execution fails
        """
        response = requests.post(
            f"{self.base_url}/db/query",
            headers=self._get_headers(),
            json={
                "database": database,
                "query": query
            }
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Query execution failed: {response.text}")

    # Privacy Portal Functions
    def list_privacy_rules(self) -> List[Dict[str, Any]]:
        """
        List all privacy rules (requires admin privileges).
        
        Returns:
            List of privacy rules
        """
        response = requests.get(
            f"{self.base_url}/privacy/rules",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to list privacy rules: {response.text}")
    
    def get_privacy_rule(self, rule_id: str) -> Dict[str, Any]:
        """
        Get a specific privacy rule by ID (requires admin privileges).
        
        Args:
            rule_id: ID of the privacy rule to retrieve
            
        Returns:
            Dict containing privacy rule details
        """
        response = requests.get(
            f"{self.base_url}/privacy/rules/{rule_id}",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to get privacy rule: {response.text}")
    
    def create_privacy_rule(self, rule_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new privacy rule (requires admin privileges).
        
        Args:
            rule_data: Dict containing privacy rule data with the following fields:
                - name: str - Name of the rule
                - description: Optional[str] - Description of the rule
                - enabled: bool - Whether the rule is enabled (default: True)
                - type: str - Type of privacy function ('input' or 'output')
                - action: str - Privacy action to apply
                - database: Optional[str] - Database to apply the rule to (leave empty to apply to all databases)
                - table_name: Optional[str] - Table to apply the rule to (leave empty to apply to all tables)
                - parameters: dict - Parameters for the privacy function
            
        Returns:
            Dict containing created privacy rule details
            
        Example:
            >>> # Create a rule to mask email addresses in the 'users' table
            >>> client.create_privacy_rule({
            ...     "name": "Mask Email Addresses",
            ...     "description": "Masks email addresses in query results",
            ...     "enabled": True,
            ...     "type": "output",
            ...     "action": "mask_columns",
            ...     "database": "main",
            ...     "table_name": "users",
            ...     "parameters": {
            ...         "columns": ["email"],
            ...         "mask_char": "*",
            ...         "show_first": 2,
            ...         "show_last": 2
            ...     }
            ... })
        """
        response = requests.post(
            f"{self.base_url}/privacy/rules",
            headers=self._get_headers(),
            json=rule_data
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to create privacy rule: {response.text}")
    
    def update_privacy_rule(self, rule_id: str, rule_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing privacy rule (requires admin privileges).
        
        Args:
            rule_id: ID of the privacy rule to update
            rule_data: Dict containing fields to update, which may include:
                - name: Optional[str] - Name of the rule
                - description: Optional[str] - Description of the rule
                - enabled: Optional[bool] - Whether the rule is enabled
                - type: Optional[str] - Type of privacy function ('input' or 'output')
                - action: Optional[str] - Privacy action to apply
                - database: Optional[str] - Database to apply the rule to (leave empty to apply to all databases)
                - table_name: Optional[str] - Table to apply the rule to (leave empty to apply to all tables)
                - parameters: Optional[dict] - Parameters for the privacy function
            
        Returns:
            Dict containing updated privacy rule details
            
        Example:
            >>> # Update a rule to apply to a specific table
            >>> client.update_privacy_rule("rule-id-123", {
            ...     "table_name": "employees",
            ...     "parameters": {
            ...         "columns": ["email", "phone_number"],
            ...         "mask_char": "#",
            ...         "show_first": 3,
            ...         "show_last": 3
            ...     }
            ... })
        """
        response = requests.put(
            f"{self.base_url}/privacy/rules/{rule_id}",
            headers=self._get_headers(),
            json=rule_data
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to update privacy rule: {response.text}")
    
    def delete_privacy_rule(self, rule_id: str) -> bool:
        """
        Delete a privacy rule (requires admin privileges).
        
        Args:
            rule_id: ID of the privacy rule to delete
            
        Returns:
            True if successful
        """
        response = requests.delete(
            f"{self.base_url}/privacy/rules/{rule_id}",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return True
        else:
            raise AuthError(f"Failed to delete privacy rule: {response.text}")
    
    def list_input_privacy_actions(self) -> List[str]:
        """
        List all available input privacy actions (requires admin privileges).
        
        Returns:
            List of input privacy action names
        """
        response = requests.get(
            f"{self.base_url}/privacy/actions/input",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to list input privacy actions: {response.text}")
    
    def list_output_privacy_actions(self) -> List[str]:
        """
        List all available output privacy actions (requires admin privileges).
        
        Returns:
            List of output privacy action names
        """
        response = requests.get(
            f"{self.base_url}/privacy/actions/output",
            headers=self._get_headers()
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise AuthError(f"Failed to list output privacy actions: {response.text}")