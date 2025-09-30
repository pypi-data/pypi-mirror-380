# Vote Summary Service

from typing import Dict, Any
from boto3_assist.dynamodb.dynamodb import DynamoDB
from .database_service import DatabaseService
from .service_result import ServiceResult
from .service_errors import ValidationError, NotFoundError
from .models.vote_summary import VoteSummary


class VoteSummaryService(DatabaseService[VoteSummary]):
    """Service for VoteSummary database operations."""
    
    def __init__(self, *, dynamodb: DynamoDB = None, table_name: str = None):
        super().__init__(dynamodb=dynamodb, table_name=table_name)
    
    def create(self, tenant_id: str, user_id: str, **kwargs) -> ServiceResult[VoteSummary]:
        """Create or update (upsert) a vote summary for a target."""
        try:
            # Validate required fields
            required_fields = ['target_id']
            self._validate_required_fields(kwargs, required_fields)

            # First check if a summary already exists for this target
            existing = self._get_by_target_id(kwargs.get('target_id'))
            if existing:
                # Update the existing summary
                updates: Dict[str, Any] = {
                    'content': kwargs.get('content', existing.content or {}),
                    'total_up_votes': kwargs.get('total_up_votes', existing.total_up_votes),
                    'total_down_votes': kwargs.get('total_down_votes', existing.total_down_votes),
                    'total_votes': kwargs.get('total_votes', existing.total_votes),
                }
                return self.update(existing.id, tenant_id, user_id, updates)
            
            # Create new vote summary instance
            summary = VoteSummary()
            summary.content = kwargs.get('content', {})
            summary.tenant_id = tenant_id
            summary.user_id = user_id
            summary.target_id = kwargs.get('target_id')
            summary.total_up_votes = int(kwargs.get('total_up_votes', 0) or 0)
            summary.total_down_votes = int(kwargs.get('total_down_votes', 0) or 0)
            summary.total_votes = int(kwargs.get('total_votes', 0) or 0)
            summary.created_by_id = user_id
            
            # Prepare for save (sets ID and timestamps)
            summary.prep_for_save()
            
            # Save to database
            return self._save_model(summary)
            
        except Exception as e:
            return self._handle_service_exception(e, 'create_vote_summary', tenant_id=tenant_id, user_id=user_id)

    def _get_by_target_id(self, target_id: str) -> VoteSummary | None:
        """Helper: get a vote summary by target_id via GSI2."""
        model = VoteSummary()
        model.target_id = target_id
        result = self._query_by_index(model, "gsi2")
        if result.success and result.data:
            return result.data[0]
        return None
    
    def get_by_id(self, resource_id: str, tenant_id: str, user_id: str) -> ServiceResult[VoteSummary]:
        """Get vote summary by ID with access control."""
        try:
            summary = self._get_model_by_id(resource_id, VoteSummary)
            
            if not summary:
                raise NotFoundError(f"VoteSummary with ID {resource_id} not found")
            
            # Validate tenant access
            if hasattr(summary, 'tenant_id'):
                self._validate_tenant_access(summary.tenant_id, tenant_id)
            
            return ServiceResult.success_result(summary)
            
        except Exception as e:
            return self._handle_service_exception(e, 'get_vote_summary', resource_id=resource_id, tenant_id=tenant_id)

    def get_by_target_id(self, target_id: str, tenant_id: str, user_id: str) -> ServiceResult[VoteSummary]:
        """Get vote summary by target_id with access control."""
        try:
            summary = self._get_by_target_id(target_id)
            
            if not summary:
                raise NotFoundError(f"VoteSummary for target {target_id} not found")
            
            # Validate tenant access
            if hasattr(summary, 'tenant_id'):
                self._validate_tenant_access(summary.tenant_id, tenant_id)
            
            return ServiceResult.success_result(summary)
            
        except Exception as e:
            return self._handle_service_exception(e, 'get_vote_summary_by_target', target_id=target_id, tenant_id=tenant_id)
    
    def update(self, resource_id: str, tenant_id: str, user_id: str, 
               updates: Dict[str, Any]) -> ServiceResult[VoteSummary]:
        """Update vote summary with access control."""
        try:
            # Get existing summary
            summary = self._get_model_by_id(resource_id, VoteSummary)
            
            if not summary:
                raise NotFoundError(f"VoteSummary with ID {resource_id} not found")
            
            # Validate tenant access
            if hasattr(summary, 'tenant_id'):
                self._validate_tenant_access(summary.tenant_id, tenant_id)
            
            # Apply updates
            for field, value in updates.items():
                if hasattr(summary, field) and field not in ['id', 'created_utc_ts', 'tenant_id']:
                    setattr(summary, field, value)
            
            # Update metadata
            summary.updated_by_id = user_id
            summary.prep_for_save()  # Updates timestamp
            
            # Save updated summary
            return self._save_model(summary)
            
        except Exception as e:
            return self._handle_service_exception(e, 'update_vote_summary', resource_id=resource_id, tenant_id=tenant_id)
    
    def delete(self, resource_id: str, tenant_id: str, user_id: str) -> ServiceResult[bool]:
        """Delete vote summary with access control."""
        try:
            summary = self._get_model_by_id(resource_id, VoteSummary)
            
            if not summary:
                raise NotFoundError(f"VoteSummary with ID {resource_id} not found")
            
            if hasattr(summary, 'tenant_id'):
                self._validate_tenant_access(summary.tenant_id, tenant_id)
            
            return self._delete_model(summary)
            
        except Exception as e:
            return self._handle_service_exception(e, 'delete_vote_summary', resource_id=resource_id, tenant_id=tenant_id)
    
    def list_by_tenant(self, tenant_id: str) -> ServiceResult[list[VoteSummary]]:
        """List vote summaries by tenant."""
        try:
            model = VoteSummary()
            model.tenant_id = tenant_id
            return self._query_by_index(model, "gsi3")
        except Exception as e:
            return self._handle_service_exception(e, 'list_vote_summaries', tenant_id=tenant_id)

    def list_all(self) -> ServiceResult[list[VoteSummary]]:
        """List all vote summaries."""
        try:
            model = VoteSummary()
            return self._query_by_index(model, "gsi1")
        except Exception as e:
            return self._handle_service_exception(e, 'list_all_vote_summaries')
