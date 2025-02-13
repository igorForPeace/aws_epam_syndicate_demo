from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        return 200
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    #return HANDLER.lambda_handler(event=event, context=context)
    path = event.get("rawPath", "")
    method = event.get("requestContext", {}).get("http", {}).get("method", "")
    if path == "/hello" and method == "GET":
        return {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
    return {
        "statusCode": 400,
        "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
    }
