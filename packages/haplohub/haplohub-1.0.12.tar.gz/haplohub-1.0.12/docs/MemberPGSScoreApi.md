# haplohub.MemberPGSScoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_member_pgs_score**](MemberPGSScoreApi.md#get_member_pgs_score) | **GET** /api/v1/member-pgs-score/{member_pgs_score_id}/ | Get member PGS score
[**list_member_pgs_scores**](MemberPGSScoreApi.md#list_member_pgs_scores) | **GET** /api/v1/member-pgs-score/ | List member PGS scores


# **get_member_pgs_score**
> GetMemberPgsScoreResponse get_member_pgs_score(member_pgs_score_id)

Get member PGS score

Retrieve a specific polygenic score calculation by its identifier.

### Example

* Bearer Authentication (Auth0JWTBearer):
```python
import time
import os
import haplohub
from haplohub.models.get_member_pgs_score_response import GetMemberPgsScoreResponse
from haplohub.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: 
configuration = haplohub.Configuration(
    access_token=os.environ["API_KEY"]
)
# Enter a context with an instance of the API client
with haplohub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = haplohub.MemberPGSScoreApi(api_client)
    member_pgs_score_id = 'member_pgs_score_id_example' # str | 

    try:
        # Get member PGS score
        api_response = api_instance.get_member_pgs_score(member_pgs_score_id)
        print("The response of MemberPGSScoreApi->get_member_pgs_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPGSScoreApi->get_member_pgs_score: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_pgs_score_id** | **str**|  | 

### Return type

[**GetMemberPgsScoreResponse**](GetMemberPgsScoreResponse.md)

### Authorization

[Auth0JWTBearer](../README.md#Auth0JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_pgs_scores**
> ListMemberPgsScoresResponse list_member_pgs_scores(cohort_id, member_id, latest=latest)

List member PGS scores

Retrieve polygenic score calculations for a cohort member.

### Example

* Bearer Authentication (Auth0JWTBearer):
```python
import time
import os
import haplohub
from haplohub.models.list_member_pgs_scores_response import ListMemberPgsScoresResponse
from haplohub.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: 
configuration = haplohub.Configuration(
    access_token=os.environ["API_KEY"]
)
# Enter a context with an instance of the API client
with haplohub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = haplohub.MemberPGSScoreApi(api_client)
    cohort_id = 'cohort_id_example' # str | 
    member_id = 'member_id_example' # str | 
    latest = False # bool |  (optional) (default to False)

    try:
        # List member PGS scores
        api_response = api_instance.list_member_pgs_scores(cohort_id, member_id, latest=latest)
        print("The response of MemberPGSScoreApi->list_member_pgs_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPGSScoreApi->list_member_pgs_scores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cohort_id** | **str**|  | 
 **member_id** | **str**|  | 
 **latest** | **bool**|  | [optional] [default to False]

### Return type

[**ListMemberPgsScoresResponse**](ListMemberPgsScoresResponse.md)

### Authorization

[Auth0JWTBearer](../README.md#Auth0JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

