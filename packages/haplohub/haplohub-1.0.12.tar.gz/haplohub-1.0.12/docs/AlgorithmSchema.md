# AlgorithmSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**owner** | **str** |  | 
**name** | **str** |  | 
**latest_version** | **str** |  | 

## Example

```python
from haplohub.models.algorithm_schema import AlgorithmSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmSchema from a JSON string
algorithm_schema_instance = AlgorithmSchema.from_json(json)
# print the JSON string representation of the object
print AlgorithmSchema.to_json()

# convert the object into a dict
algorithm_schema_dict = algorithm_schema_instance.to_dict()
# create an instance of AlgorithmSchema from a dict
algorithm_schema_from_dict = AlgorithmSchema.from_dict(algorithm_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


