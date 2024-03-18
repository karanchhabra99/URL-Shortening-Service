# URL Shortener Service

This project is a URL shortening service built on AWS services. It provides a secure and scalable solution to create, delete, and redirect shortened URLs.

## Architecture

The system uses AWS Cognito for user authentication, allowing users to interact with the AWS API Gateway. The API Gateway can trigger any of the three AWS Lambda functions:

1. **Shorten URL Generator**: Generates a shortened URL for a given original URL.
2. **Delete Shorten URL**: Deletes a previously generated shortened URL.
3. **Redirect to Original URL**: Redirects a request from the shortened URL to the original URL.

All three Lambda functions interact with DynamoDB for data storage and retrieval.
![Architecture](url_shortener_system.png)

## Features

- **User Authentication**: AWS Cognito is used for secure user authentication.
- **URL Shortening**: Generate a unique shortened URL for any given URL.
- **URL Deletion**: Delete a previously shortened URL.
- **URL Redirection**: Redirect from the shortened URL to the original URL.
- **Scalability and Performance**: The system is built on AWS services, ensuring high scalability and performance.

## Learning
1. Redirecting using HTTP request instead of HTML static pages
HTML: https://redirect-sug.s3.us-west-2.amazonaws.com/d1B5LQLiMNL
HTTP: https://sqvreaj3o7.execute-api.us-west-2.amazonaws.com/dev/SSWDZBFFxSS

![Old Architecture](Earlier%20Approach%20-%20url_shortener_system.png)

2. Lambda concurrency

## Reference
- High Level System Design: https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers/system-design-tinyurl
- Hosting a static S3 Website: https://www.youtube.com/watch?v=-l83oqcaTHg
- AWS Cognito: https://www.youtube.com/watch?v=8a0vtkWJIA4
- AWS Cognito - Email Extraction: https://www.youtube.com/watch?v=ALgbhPaMT1M
- API Gateway Authentication: https://www.youtube.com/watch?v=9crTLAT_4uY
- IAM: https://www.youtube.com/watch?v=iF9fs8Rw4Uo
- Cognito Authentication: https://github.com/aws-amplify/amplify-js/tree/master/packages/amazon-cognito-identity-js