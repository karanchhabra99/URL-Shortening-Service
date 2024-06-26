
# from diagrams import Cluster, Diagram, Edge

# from diagrams.aws.database import Dynamodb
# from diagrams import Cluster, Diagram
# from diagrams.aws.compute import Lambda
# from diagrams.aws.network import APIGateway, CloudFront
# from diagrams.aws.security import Cognito
# from diagrams.aws.storage import S3
# from diagrams.onprem.client import User

# with Diagram("URL Shortener System"):
#     with Cluster("Client"):
#         client = User("Client")
#     with Cluster("User Interface (UI)"):
#         ui = S3("Static Website")
#         cf = CloudFront("CloudFront")
#         client >> cf >> ui
#     api_gateway = APIGateway("API Gateway")
#     cognito = Cognito("Cognito")
#     dynamodb = Dynamodb("DynamoDB")
#     with Cluster("Lambda Functions"):
#         lambda_functions = [Lambda("URL Shortening"), Lambda("URL Deletion")]
#     redirect = S3("Re-direct Website")
#     # ui >> api_gateway >> lambda_functions[0] >> dynamodb
#     # Redirect >> dynamodb
#     # ui >> Edge(style="invis", minlen=4) >> lambda_functions[0] 
#     # lambda_functions[1] >> dynamodb
#     # lambda_functions[2] >> dynamodb
#     # lambda_functions[2] >> ui
#     # ui >> Edge(style="invis", minlen=1) >> lambda_functions   
#     # lambda_functions >> ui
#     ui >> cognito
#     cf >> redirect

#     ui >> api_gateway >>  lambda_functions >> dynamodb
#     lambda_functions >> redirect
#     api_gateway >> Edge(style="invis", minlen=1) >> ui

from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.security import Cognito
from diagrams.onprem.client import User
from diagrams.aws.storage import S3

with Diagram("URL Shortener System - Create and Delete", show=True):
    user = User("Client")
    AWS_Cognito = Cognito("AWS_Cognito")

    with Cluster("User Interface (UI)"):
        ui = S3("Static Website")
        # cf = CloudFront("CloudFront")
        user >>  ui

    with Cluster("Shorten URL Service"):
        rest_api_gateway = APIGateway("REST API Gateway")
        # http_api_gateway = APIGateway("HTTP API Gateway")
        shorten_url_lambda = Lambda("Shorten URL")
        delete_url_lambda = Lambda("Delete URL")
        # redirect_url_lambda = Lambda("Redirect URL")
        dynamodb = Dynamodb("DynamoDB")

    ui >> AWS_Cognito
    ui >> rest_api_gateway >> shorten_url_lambda >> dynamodb
    rest_api_gateway >> delete_url_lambda >> dynamodb
    # ui >> http_api_gateway >> redirect_url_lambda >> dynamodb



with Diagram("URL Shortener System - Redirect", show=True):
    user = User("Client")
    # AWS_Cognito = Cognito("AWS_Cognito")

    with Cluster("User Interface (UI)"):
        ui = S3("Static Website")
        # cf = CloudFront("CloudFront")
        user >>  ui

    with Cluster("Shorten URL Service"):
        # rest_api_gateway = APIGateway("REST API Gateway")
        http_api_gateway = APIGateway("HTTP API Gateway")
        # shorten_url_lambda = Lambda("Shorten URL")
        # delete_url_lambda = Lambda("Delete URL")
        redirect_url_lambda = Lambda("Redirect URL")
        dynamodb = Dynamodb("DynamoDB")

    # ui >> AWS_Cognito
    # ui >> rest_api_gateway >> shorten_url_lambda >> dynamodb
    # rest_api_gateway >> delete_url_lambda >> dynamodb
    ui >> http_api_gateway >> redirect_url_lambda >> dynamodb
