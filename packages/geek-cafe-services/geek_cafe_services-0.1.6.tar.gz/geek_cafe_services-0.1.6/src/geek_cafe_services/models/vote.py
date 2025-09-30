
from boto3_assist.dynamodb.dynamodb_index import DynamoDBIndex, DynamoDBKey
from boto3_assist.utilities.string_utility import StringUtility
import datetime as dt
from typing import Dict, Any
from geek_cafe_services.models.base_model import BaseModel

class Vote(BaseModel):
    def __init__(self):
        super().__init__()
        self._content: Dict[str, Any]= {}
        self._up_vote: int = 0
        self._down_vote: int = 0
        self._target_id: str | None = None

        self._setup_indexes()

    def _setup_indexes(self):
        primary: DynamoDBIndex = DynamoDBIndex()
        primary.name = "primary"
        primary.partition_key.attribute_name = "pk"
        primary.partition_key.value = lambda: DynamoDBKey.build_key(
            ("vote", self.id)
        )

        primary.sort_key.attribute_name = "sk"
        primary.sort_key.value = lambda: DynamoDBKey.build_key(("vote", self.id))
        self.indexes.add_primary(primary)
        
        ## GSI: 1
        # GSI: all votes
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi1"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("vote", "all"))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 2
        # GSI: all votes by user, sorted by created ts
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi2"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("user", self.user_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("model", "vote"),("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 3
        # GSI: all votes by tenant, sorted by created ts
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi3"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("tenant", self.tenant_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("model", "vote"),("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 4
        # GSI: enforce uniqueness helper - all votes by user+target (one per target per user)
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi4"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("user", self.user_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("target", self.target_id)
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 5
        # GSI: all votes for a target
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi5"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("target", self.target_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

    @property
    def content(self) -> Dict[str, Any]:
        return self._content

    @content.setter
    def content(self, value: Dict[str, Any]):
        self._content = value
    
    @property
    def up_vote(self) -> int:
        return self._up_vote
    
    @up_vote.setter
    def up_vote(self, value: int):
        self._up_vote = value
    
    @property
    def down_vote(self) -> int:
        return self._down_vote
    
    @down_vote.setter
    def down_vote(self, value: int):
        self._down_vote = value
    
    @property
    def target_id(self) -> str | None:
        return self._target_id
    
    @target_id.setter
    def target_id(self, value: str | None):
        self._target_id = value