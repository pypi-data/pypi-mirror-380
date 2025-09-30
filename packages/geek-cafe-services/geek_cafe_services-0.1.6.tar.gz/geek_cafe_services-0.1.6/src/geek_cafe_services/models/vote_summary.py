
from boto3_assist.dynamodb.dynamodb_index import DynamoDBIndex, DynamoDBKey
from boto3_assist.utilities.string_utility import StringUtility
import datetime as dt
from typing import Dict, Any
from geek_cafe_services.models.base_model import BaseModel

class VoteSummary(BaseModel):
    def __init__(self):
        super().__init__()
        self._content: Dict[str, Any]= {}
        self._total_up_votes: int = 0
        self._total_down_votes: int = 0
        self._total_votes: int = 0
        self._target_id: str | None = None

        self._setup_indexes()

    def _setup_indexes(self):
        primary: DynamoDBIndex = DynamoDBIndex()
        primary.name = "primary"
        primary.partition_key.attribute_name = "pk"
        primary.partition_key.value = lambda: DynamoDBKey.build_key(
            ("vote-summary", self.id)
        )

        primary.sort_key.attribute_name = "sk"
        primary.sort_key.value = lambda: DynamoDBKey.build_key(("vote-summary", self.id))
        self.indexes.add_primary(primary)
        
        ## GSI: 1
        # GSI: all vote summaries
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi1"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("vote-summary", "all"))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 2
        # GSI: vote summary by target_id (for quick lookup by target)
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi2"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("target", self.target_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("model", "vote-summary")
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 3
        # GSI: vote summaries by tenant
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi3"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("tenant", self.tenant_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("model", "vote-summary"),("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

        

    @property
    def content(self) -> Dict[str, Any]:
        return self._content

    @content.setter
    def content(self, value: Dict[str, Any]):
        self._content = value
    
    
    @property
    def total_up_votes(self) -> int:
        return self._total_up_votes
    
    @total_up_votes.setter
    def total_up_votes(self, value: int):
        self._total_up_votes = value

    @property
    def total_down_votes(self) -> int:
        return self._total_down_votes
    
    @total_down_votes.setter
    def total_down_votes(self, value: int):
        self._total_down_votes = value
    
    @property
    def total_votes(self) -> int:
        return self._total_votes
    
    @total_votes.setter
    def total_votes(self, value: int):
        self._total_votes = value
    
    @property
    def target_id(self) -> str | None:
        return self._target_id

    @target_id.setter
    def target_id(self, value: str | None):
        self._target_id = value