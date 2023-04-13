"""status provides HTTP status codes and their meanings. It contains four
classes for HTTP status codes: Informational, Success, Redirection, and
ClientError. Each class is an IntEnum that defines the HTTP status codes as
class members and gives them integer values. The integer values are the
numeric HTTP status codes. The Informational class represents
HTTP status codes in the 1xx range, the Success class represents status codes
in the 2xx range, the Redirection class represents status codes in the
3xx range, and the ClientError class represents status codes
in the 4xx range."""
from enum import Enum


class Informational(int, Enum):
    """`Informational`: class defines three HTTP status codes:
    `CONTINUE`, `SWITCHING_PROTOCOLS`, and `PROCESSING`."""

    # The server has received the request headers and the client should
    # proceed to send the request body.
    CONTINUE: int = 100

    # The requester has asked the server to switch protocols and the
    # server has agreed to do so.
    SWITCHING_PROTOCOLS: int = 101

    # The server is processing the request but has not yet completed it.
    PROCESSING: int = 102


class Success(int, Enum):
    """`Success`: class defines nine HTTP status codes:
    `OK`, `CREATED`, `ACCEPTED`, `NON_AUTHORITATIVE_INFORMATION`,
    `NO_CONTENT`, `RESET_CONTENT`, `PARTIAL_CONTENT`,
    `MULTI_STATUS`, and `IM_USED`."""

    # The request was successful.
    OK: int = 200

    # The request has been fulfilled, resulting in the
    # creation of a new resource.
    CREATED: int = 201

    # The request has been accepted for processing, but the processing
    # has not been completed.
    ACCEPTED: int = 202

    # The server is a transforming proxy that received a 200 OK from
    # its origin, but is returning a modified version.
    NON_AUTHORITATIVE_INFORMATION: int = 203

    # The server has successfully fulfilled the request and there is
    # no additional content to send in the response.
    NO_CONTENT: int = 204

    # The server has fulfilled the request and the user agent should reset the
    # document view which caused the request to be sent.
    RESET_CONTENT: int = 205

    # The server has fulfilled the partial GET request for the resource.
    PARTIAL_CONTENT: int = 206

    # The message body that follows is an XML message and can contain a
    # number of separate response codes, depending on how many
    # sub-requests were made.
    MULTI_STATUS: int = 207

    # The server has fulfilled a GET request for the resource,
    # and the response is a representation of the result of one or more
    # instance-manipulations applied to the current instance.
    IM_USED: int = 226


class Redirection(int, Enum):
    """`Redirection`: class defines seven HTTP status codes:
    `MULTIPLE_CHOICES`, `MOVED_PERMANENTLY`, `FOUND`, `SEE_OTHER`,
    `NOT_MODIFIED`, `USE_PROXY`, and `TEMPORARY_REDIRECT`."""

    # The request has more than one possible response.
    MULTIPLE_CHOICES: int = 300

    # The URL of the requested resource has been changed permanently.
    MOVED_PERMANENTLY: int = 301

    # The URL of the requested resource has been changed temporarily.
    FOUND: int = 302

    # The response to the request can be found under a different URL.
    SEE_OTHER: int = 303

    # The requested resource has not been modified since the
    # last time the client accessed it.
    NOT_MODIFIED: int = 304

    # The requested resource must be accessed through the
    # proxy given by the Location field.
    USE_PROXY: int = 305

    # The requested resource is temporarily moved to the URL
    # given by the Location header.
    TEMPORARY_REDIRECT: int = 307


class ClientError(int, Enum):
    """`ClientError`: class defines twenty HTTP status codes: `BAD_REQUEST`,
    `UNAUTHORIZED`, `PAYMENT_REQUIRED`, `FORBIDDEN`, `NOT_FOUND`,
    `METHOD_NOT_ALLOWED`, `NOT_ACCEPTABLE`, `PROXY_AUTHENTICATION_REQUIRED`,
    `REQUEST_TIMEOUT`, `CONFLICT`, `GONE`, `LENGTH_REQUIRED`,
    `PRECONDITION_FAILED`, `REQUEST_ENTITY_TOO_LARGE`, `REQUEST_URI_TOO_LONG`,
    `UNSUPPORTED_MEDIA_TYPE`, `REQUESTED_RANGE_NOT_SATISFIABLE`,
    `EXPECTATION_FAILED`, `MISDIRECTED_REQUEST`, and
    `UNPROCESSABLE_ENTITY`."""

    # The request could not be understood or was missing required parameters.
    BAD_REQUEST: int = 400

    # Authentication failed or user does not have permissions
    # for the requested operation.
    UNAUTHORIZED: int = 401

    # Reserved for future use.
    PAYMENT_REQUIRED: int = 402

    # The client does not have access rights to the content.
    FORBIDDEN: int = 403

    # The requested resource could not be found.
    NOT_FOUND: int = 404

    # The request method is not supported for the requested resource.
    METHOD_NOT_ALLOWED: int = 405

    # The requested resource is capable of generating only content
    # not acceptable according to the Accept headers sent in the request.
    NOT_ACCEPTABLE: int = 406

    # The client must first authenticate itself with the proxy.
    PROXY_AUTHENTICATION_REQUIRED: int = 407

    # The server timed out waiting for the request.
    REQUEST_TIMEOUT: int = 408

    # The request could not be completed due to a conflict with the
    # current state of the resource.
    CONFLICT: int = 409

    # The requested resource is no longer available at the server and
    # no forwarding address is known.
    GONE: int = 410

    # The server refuses to accept the request without
    # a defined Content-Length.
    LENGTH_REQUIRED: int = 411

    # One or more conditions given in the request header fields evaluated
    # to false when tested on the server.
    PRECONDITION_FAILED: int = 412

    # The server is refusing to process a request because the
    # request payload is larger than the server is willing or able to process.
    REQUEST_ENTITY_TOO_LARGE: int = 413

    # The server is refusing to service the request because the request-target
    # is longer than the server is willing to interpret.
    REQUEST_URI_TOO_LONG: int = 414

    # The origin server is refusing to service the request because the payload
    # is in a format not supported by this method on the target resource.
    UNSUPPORTED_MEDIA_TYPE: int = 415

    # A server SHOULD return a response with this status code if a request
    # included a Range request-header field (section 14.35), and none of the
    # range-specifier values in this field overlap the current extent of the
    # selected resource, and the request did not include an
    # If-Range request-header field.
    REQUESTED_RANGE_NOT_SATISFIABLE: int = 416

    # The expectation given in an Expect request-header field
    # could not be met by this server.
    EXPECTATION_FAILED: int = 417

    # The request was well-formed but was unable to be followed
    # due to semantic errors.
    UNPROCESSABLE_ENTITY: int = 422

    # The resource that is being accessed is locked.
    LOCKED: int = 423

    # The request failed due to failure of a previous request.
    FAILED_DEPENDENCY: int = 424

    # The server refuses to perform the request using the current protocol but
    # might be willing to do so after the client upgrades
    # to a different protocol.
    UPGRADE_REQUIRED: int = 426

    # The origin server requires the request to be conditional.
    PRECONDITION_REQUIRED: int = 428

    # The user has sent too many requests in a given amount of time.
    TOO_MANY_REQUESTS: int = 429

    # The server is unwilling to process the request because either
    # an individual header field, or all the header fields collectively,
    # are too large.
    REQUEST_HEADER_FIELDS_TOO_LARGE: int = 431


class ServerError(int, Enum):
    """`ServerError`: class defines nine HTTP status codes:
    `INTERNAL_SERVER_ERROR`, `NOT_IMPLEMENTED`, `BAD_GATEWAY`,
    `SERVICE_UNAVAILABLE`, `GATEWAY_TIMEOUT`, `HTTP_VERSION_NOT_SUPPORTED`,
    `INSUFFICIENT_STORAGE`, `NOT_EXTENDED`, and
    `NETWORK_AUTHENTICATION_REQUIRED`."""

    # The server encountered an error while processing the request.
    INTERNAL_SERVER_ERROR: int = 500

    # The server does not support the functionality required to
    # fulfill the request.
    NOT_IMPLEMENTED: int = 501

    # The server, while acting as a gateway or proxy, received
    # an invalid response from an upstream server it
    # accessed to fulfill the request.
    BAD_GATEWAY: int = 502

    # The server is currently unable to handle the request due to a temporary
    # overload or maintenance of the server.
    SERVICE_UNAVAILABLE: int = 503

    # The server, while acting as a gateway or proxy, did not receive a timely
    # response from an upstream server it accessed to fulfill the request.
    GATEWAY_TIMEOUT: int = 504

    # The server does not support, or refuses to support, the protocol version
    # that was used in the request message.
    HTTP_VERSION_NOT_SUPPORTED: int = 505

    # The server is unable to store the representation needed
    # to complete the request.
    INSUFFICIENT_STORAGE: int = 507

    # The policy for accessing the resource has not been met in the request.
    # The server should send back all the information necessary for the client
    # to issue an extended request.
    NOT_EXTENDED: int = 510

    # The client needs to authenticate to gain network access.
    NETWORK_AUTHENTICATION_REQUIRED: int = 511
