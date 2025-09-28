
from boto3_assist.dynamodb.dynamodb_index import DynamoDBIndex, DynamoDBKey
from boto3_assist.utilities.string_utility import StringUtility
import datetime as dt
from typing import Dict, Any
from geek_cafe_services.models.base_model import BaseModel

class Message(BaseModel):
    def __init__(self):
        super().__init__()
        self._type: str | None = None
        self._data: Dict[str, Any]= {}
        

        self._setup_indexes()

    def _setup_indexes(self):
        primary: DynamoDBIndex = DynamoDBIndex()
        primary.name = "primary"
        primary.partition_key.attribute_name = "pk"
        primary.partition_key.value = lambda: DynamoDBKey.build_key(
            ("message", self.id)
        )

        primary.sort_key.attribute_name = "sk"
        primary.sort_key.value = lambda: DynamoDBKey.build_key(("message", self.id))
        self.indexes.add_primary(primary)
        
        ## GSI: 1
        # GSI: all messages
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi1"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("message", "all"))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 2
        # GSI: all messages by type, sorted by created ts
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi2"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("message", self.type))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)


        ## GSI: 3
        # GSI: all messages by user, sorted by created ts
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi3"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("user", self.user_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("model", "message"),("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

        ## GSI: 4
        # GSI: all messages by tenant, sorted by created ts
        gsi: DynamoDBIndex = DynamoDBIndex()
        
        gsi.name = "gsi4"
        gsi.partition_key.attribute_name = f"{gsi.name}_pk"
        gsi.partition_key.value = lambda: DynamoDBKey.build_key(("tenant", self.tenant_id))
        gsi.sort_key.attribute_name = f"{gsi.name}_sk"
        gsi.sort_key.value = lambda: DynamoDBKey.build_key(
           ("model", "message"),("ts", self.created_utc_ts)
        )
        self.indexes.add_secondary(gsi)

    @property
    def type(self) -> str | None:
        return self._type

    @type.setter
    def type(self, value: str | None):
        self._type = value

    @property
    def data(self) -> Dict[str, Any]:
        return self._data

    @data.setter
    def data(self, value: Dict[str, Any]):
        self._data = value
    
    def to_dictionary(self) -> Dict[str, Any]:
        """
        Override to flatten the data structure for cleaner API responses.
        Instead of nested data->data, flatten message-specific fields to the top level.
        """
        print("🔧 Message.to_dictionary() called - flattening structure")
        # Get the base dictionary from parent
        base_dict = super().to_dictionary()
        print(f"🔧 Base dict keys: {list(base_dict.keys())}")
        
        # Remove the nested 'data' field and flatten its contents
        if 'data' in base_dict and isinstance(base_dict['data'], dict):
            print("🔧 Flattening data field")
            data_contents = base_dict.pop('data')
            # Merge the data contents into the base dictionary
            base_dict.update(data_contents)
            print(f"🔧 After flattening keys: {list(base_dict.keys())}")
        
        return base_dict