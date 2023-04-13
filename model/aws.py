"""aws module that defines a set of TypedDict classes representing
a request and its context in a serverless application."""
from typing import Any, AnyStr, Dict, Optional, TypedDict
from uuid import UUID


class ContextIdentity(TypedDict):
    """ContextIdentity: This class represents the identity of the caller
    making the request. It is a subclass of TypedDict."""

    # accessKey: This attribute is an optional string representing the
    # access key used to make the request.
    accessKey: Optional[str]
    # accountId: This attribute is an optional string representing the AWS
    # account ID associated with the request.
    accountId: Optional[str]
    # accountId: This attribute is an optional string representing the AWS
    # account ID associated with the request.
    caller: Optional[str]
    # cognitoAuthenticationProvider: This attribute is an optional string
    # representing the authentication provider used
    # to authenticate the request.
    cognitoAuthenticationProvider: Optional[str]
    # cognitoAuthenticationType: This attribute is an optional string
    # representing the type of authentication used to authenticate the request.
    cognitoAuthenticationType: Optional[str]
    # cognitoIdentityId: This attribute is an optional string representing the
    # Cognito identity ID associated with the request.
    cognitoIdentityId: Optional[str]
    # cognitoIdentityPoolId: This attribute is an optional string representing
    # the Cognito identity pool ID associated with the request.
    cognitoIdentityPoolId: Optional[str]
    # sourceIp: This attribute is a required string representing the IP
    # address of the caller making the request.
    sourceIp: str
    # user: This attribute is an optional string representing the identity of
    # the user making the request.
    user: Optional[str]
    # userAgent: This attribute is a required string representing the user
    # agent of the client making the request.
    userAgent: str
    # userArn: This attribute is an optional string representing the ARN of
    # the user making the request.
    userArn: Optional[str]


class RequestContext(TypedDict):
    """RequestContext: This class represents the context of the request.
    It is a subclass of TypedDict."""

    # accountId: This attribute is a required string representing the
    # AWS account ID associated with the request.
    accountId: str
    # apiId: This attribute is a required string representing the ID
    # of the API Gateway instance.
    apiId: str
    # httpMethod: This attribute is a required string representing
    # the HTTP method used in the request.
    httpMethod: str
    # identity: This attribute is a required ContextIdentity object
    # representing the identity of the caller making the request.
    identity: ContextIdentity
    # path: This attribute is a required string representing the
    # path of the request.
    path: str
    # protocol: This attribute is a required string representing the protocol
    # used in the request.
    protocol: str
    # requestId: This attribute is a required string or UUID object
    # representing the ID of the request.
    requestId: (str | UUID)
    # requestTime: This attribute is a required string representing the
    # date and time the request was received.
    requestTime: str
    # requestTimeEpoch: This attribute is a required integer representing the
    # epoch time the request was received.
    requestTimeEpoch: int
    # resourceId: This attribute is a required integer representing the ID
    # of the resource associated with the request.
    resourceId: int
    # resourcePath: This attribute is a required string representing the path
    # of the resource associated with the request.
    resourcePath: str
    # stage: This attribute is a required string representing
    # the stage of the request.
    stage: str


class Request(TypedDict):
    """Request: This class represents the request itself.
    It is a subclass of TypedDict."""

    # body: This attribute is a string or bytes-like object representing
    # the body of the request.
    body: AnyStr
    # headers: This attribute is a dictionary of strings representing
    # the headers of the request.
    headers: Dict[str, Any]
    # headers: This attribute is a dictionary of strings representing
    # the headers of the request.
    httpMethod: str
    # isBase64Encoded: This attribute is a boolean indicating whether the body
    # of the request is Base64-encoded.
    isBase64Encoded: bool
    # path: This attribute is a required string representing the
    # path of the request.
    path: str
    # queryStringParameters: This attribute is a dictionary representing the
    # query string parameters of the request.
    queryStringParameters: Dict[str, Any]
    # requestContext: This attribute is a RequestContext object representing
    # the context of the request.
    requestContext: RequestContext
    # resource: This attribute is a required string representing the resource
    # associated with the request.
    resource: str
    # stageVariables: This attribute is a dictionary representing the stage.
    stageVariables: Dict[str, Any]
