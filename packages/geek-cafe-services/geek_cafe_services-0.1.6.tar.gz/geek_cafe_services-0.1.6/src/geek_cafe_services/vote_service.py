# Vote Service

from typing import Dict, Any
from boto3_assist.dynamodb.dynamodb import DynamoDB
from .database_service import DatabaseService
from .service_result import ServiceResult
from .service_errors import ValidationError, NotFoundError
from .models.vote import Vote


class VoteService(DatabaseService[Vote]):
    """Service for Vote database operations."""
    
    def __init__(self, *, dynamodb: DynamoDB = None, table_name: str = None):
        super().__init__(dynamodb=dynamodb, table_name=table_name)
    
    def create(self, tenant_id: str, user_id: str, **kwargs) -> ServiceResult[Vote]:
        """Create or update (upsert) a vote for a target by a user."""
        try:
            # Validate required fields
            required_fields = ['target_id']
            self._validate_required_fields(kwargs, required_fields)

            # First check if a vote already exists for this user+target
            existing = self._get_by_user_and_target(user_id, kwargs.get('target_id'))
            if existing:
                # Update the existing vote
                updates: Dict[str, Any] = {
                    'content': kwargs.get('content', existing.content or {}),
                    'up_vote': kwargs.get('up_vote', existing.up_vote),
                    'down_vote': kwargs.get('down_vote', existing.down_vote),
                }
                return self.update(existing.id, tenant_id, user_id, updates)
            
            # Create new vote instance
            vote = Vote()
            vote.content = kwargs.get('content', {})
            vote.tenant_id = tenant_id
            vote.user_id = user_id
            vote.target_id = kwargs.get('target_id')
            vote.up_vote = int(kwargs.get('up_vote', 0) or 0)
            vote.down_vote = int(kwargs.get('down_vote', 0) or 0)
            vote.created_by_id = user_id
            
            # Prepare for save (sets ID and timestamps)
            vote.prep_for_save()
            
            # Save to database
            return self._save_model(vote)
            
        except Exception as e:
            return self._handle_service_exception(e, 'create_vote', tenant_id=tenant_id, user_id=user_id)

    def _get_by_user_and_target(self, user_id: str, target_id: str) -> Vote | None:
        """Helper: get a vote by user and target via GSI4."""
        model = Vote()
        model.user_id = user_id
        model.target_id = target_id
        result = self._query_by_index(model, "gsi4")
        if result.success and result.data:
            return result.data[0]
        return None
    
    def get_by_id(self, resource_id: str, tenant_id: str, user_id: str) -> ServiceResult[Vote]:
        """Get vote by ID with access control."""
        try:
            vote = self._get_model_by_id(resource_id, Vote)
            
            if not vote:
                raise NotFoundError(f"Vote with ID {resource_id} not found")
            
            # Validate tenant access
            if hasattr(vote, 'tenant_id'):
                self._validate_tenant_access(vote.tenant_id, tenant_id)
            
            return ServiceResult.success_result(vote)
            
        except Exception as e:
            return self._handle_service_exception(e, 'get_vote', resource_id=resource_id, tenant_id=tenant_id)
    
    def update(self, resource_id: str, tenant_id: str, user_id: str, 
               updates: Dict[str, Any]) -> ServiceResult[Vote]:
        """Update vote with access control."""
        try:
            # Get existing vote
            vote = self._get_model_by_id(resource_id, Vote)
            
            if not vote:
                raise NotFoundError(f"Vote with ID {resource_id} not found")
            
            # Validate tenant access
            if hasattr(vote, 'tenant_id'):
                self._validate_tenant_access(vote.tenant_id, tenant_id)
            
            # Apply updates
            for field, value in updates.items():
                if hasattr(vote, field) and field not in ['id', 'created_utc_ts', 'tenant_id']:
                    setattr(vote, field, value)
            
            # Update metadata
            vote.updated_by_id = user_id
            vote.prep_for_save()  # Updates timestamp
            
            # Save updated vote
            return self._save_model(vote)
            
        except Exception as e:
            return self._handle_service_exception(e, 'update_vote', resource_id=resource_id, tenant_id=tenant_id)
    
    def delete(self, resource_id: str, tenant_id: str, user_id: str) -> ServiceResult[bool]:
        """Delete vote with access control."""
        try:
            vote = self._get_model_by_id(resource_id, Vote)
            
            if not vote:
                raise NotFoundError(f"Vote with ID {resource_id} not found")
            
            if hasattr(vote, 'tenant_id'):
                self._validate_tenant_access(vote.tenant_id, tenant_id)
            
            return self._delete_model(vote)
            
        except Exception as e:
            return self._handle_service_exception(e, 'delete_vote', resource_id=resource_id, tenant_id=tenant_id)
    
    def list_by_user(self, user_id: str, ascending: bool = False) -> ServiceResult[list[Vote]]:
        """List votes by user."""
        try:
            model = Vote()
            model.user_id = user_id
            return self._query_by_index(model, "gsi2", ascending=ascending)
        except Exception as e:
            return self._handle_service_exception(e, 'list_votes', user_id=user_id)

    def list_by_tenant(self, tenant_id: str) -> ServiceResult[list[Vote]]:
        """List votes by tenant."""
        try:
            model = Vote()
            model.tenant_id = tenant_id
            return self._query_by_index(model, "gsi3")
        except Exception as e:
            return self._handle_service_exception(e, 'list_votes', tenant_id=tenant_id)

    def list_by_target(self, target_id: str, *, start_key: dict = None, limit: int = None) -> ServiceResult[list[Vote]]:
        """List votes by target with optional pagination."""
        try:
            model = Vote()
            model.target_id = target_id
            return self._query_by_index(model, "gsi5", start_key=start_key, limit=limit)
        except Exception as e:
            return self._handle_service_exception(e, 'list_votes', target_id=target_id)
