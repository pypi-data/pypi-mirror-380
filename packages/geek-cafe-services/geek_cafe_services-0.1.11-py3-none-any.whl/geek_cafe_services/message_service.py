# Message Service

from typing import Dict, Any, Optional
from boto3_assist.dynamodb.dynamodb import DynamoDB
from .database_service import DatabaseService
from .service_result import ServiceResult
from .service_errors import ValidationError, NotFoundError
from .models.message import Message


class MessageService(DatabaseService[Message]):
    """Service for Message database operations."""
    
    def __init__(self, *, dynamodb: DynamoDB = None, table_name: str = None):
        super().__init__(dynamodb=dynamodb, table_name=table_name)
    
    def create(self, tenant_id: str, user_id: str, **kwargs) -> ServiceResult[Message]:
        """Create a new message."""
        try:
            # Validate required fields
            required_fields = ['type']
            self._validate_required_fields(kwargs, required_fields)
            
            # Create message instance
            message = Message()
            message.type = kwargs.get('type')
            message.content = kwargs.get('content', {})
            message.tenant_id = tenant_id
            message.user_id = user_id
            message.created_by_id = user_id
            
            # Prepare for save (sets ID and timestamps)
            message.prep_for_save()
            
            # Save to database
            return self._save_model(message)
            
        except Exception as e:
            return self._handle_service_exception(e, 'create_message', tenant_id=tenant_id, user_id=user_id)
    
    def get_by_id(self, resource_id: str, tenant_id: str, user_id: str) -> ServiceResult[Message]:
        """Get message by ID with access control."""
        try:
            message = self._get_model_by_id(resource_id, Message)
            
            if not message:
                raise NotFoundError(f"Message with ID {resource_id} not found")
            
            # Validate tenant access
            if hasattr(message, 'tenant_id'):
                self._validate_tenant_access(message.tenant_id, tenant_id)
            
            return ServiceResult.success_result(message)
            
        except Exception as e:
            return self._handle_service_exception(e, 'get_message', resource_id=resource_id, tenant_id=tenant_id)
    
    def update(self, resource_id: str, tenant_id: str, user_id: str, 
               updates: Dict[str, Any]) -> ServiceResult[Message]:
        """Update message with access control."""
        try:
            # Get existing message
            message = self._get_model_by_id(resource_id, Message)
            
            if not message:
                raise NotFoundError(f"Message with ID {resource_id} not found")
            
            # Validate tenant access
            if hasattr(message, 'tenant_id'):
                self._validate_tenant_access(message.tenant_id, tenant_id)
            
            # Apply updates
            for field, value in updates.items():
                if hasattr(message, field) and field not in ['id', 'created_utc_ts', 'tenant_id']:
                    setattr(message, field, value)
            
            # Update metadata
            message.updated_by_id = user_id
            message.prep_for_save()  # Updates timestamp
            
            # Save updated message
            return self._save_model(message)
            
        except Exception as e:
            return self._handle_service_exception(e, 'update_message', resource_id=resource_id, tenant_id=tenant_id)
    
    def delete(self, resource_id: str, tenant_id: str, user_id: str) -> ServiceResult[bool]:
        """Delete message with access control."""
        try:
            # Get existing message
            message = self._get_model_by_id(resource_id, Message)
            
            if not message:
                raise NotFoundError(f"Message with ID {resource_id} not found")
            
            # Validate tenant access
            if hasattr(message, 'tenant_id'):
                self._validate_tenant_access(message.tenant_id, tenant_id)
            
            # Delete the message
            return self._delete_model(message)
            
        except Exception as e:
            return self._handle_service_exception(e, 'delete_message', resource_id=resource_id, tenant_id=tenant_id)
    
    def list_by_user(self, user_id: str, ascending: bool = False) -> ServiceResult[list[Message]]:
        """List messages by user."""
        try:
            model = Message()
            model.user_id = user_id
            return self._query_by_index(model, "gsi3", ascending=ascending)
            
        except Exception as e:
            return self._handle_service_exception(e, 'list_messages', user_id=user_id)

    def list_by_tenant(self, tenant_id: str) -> ServiceResult[list[Message]]:
        """List messages by tenant."""
        try:
            model = Message()
            model.tenant_id = tenant_id
            return self._query_by_index(model, "gsi4")
            
        except Exception as e:
            return self._handle_service_exception(e, 'list_messages', tenant_id=tenant_id)

    def list_by_type(self, message_type: str) -> ServiceResult[list[Message]]:
        """List messages by type."""
        try:
            model = Message()
            model.type = message_type
            return self._query_by_index(model, "gsi2")
            
        except Exception as e:
            return self._handle_service_exception(e, 'list_messages', message_type=message_type)