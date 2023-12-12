# LLM Demo

This repo contains a demonstration of an application that interfaces with a
Large Language Model (LLM). The application allows users to prompt through a
simplified interface.

## Case
The case imaginged for this demonstration, is a scenario where a colleague needs to summarrise complaints that they recieve. Reading hundreds of angry mails causes stress and lowers productivity. We really just need to know what the defects are.

Our company manufactures glassware and we send out many defect units.

## Running the Demonstration
create `.env` file with AWS credentials for a user with proper policies to access AWS Bedrock.

The `.env` file should contain the following fields:

```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION =
```

The application is built using `docker-compose`, so the application can be run with a single command:

```
docker-compose up
``` 

The application is exposed on port `8040`.

The file `complaints.txt` contains a set of sample complaints that can be used for demonstration prompts.

## Stack
The application was build with `FastAPI` augmented by `Pydantic` for input and response validation.

The chosen LLM is `Jurassic-2 Ultra` which is one of the foundational models provided by AWS Bedrock.

The application is built using `docker-compose` for easy demonstration and deployment.

Additional Python dependencies are listed in Additional requirements are listed in `requirements.txt`. Most notable are `boto3`, the AWS SDK for Python, and `uvicorn` for hosting the application.

## Todo
Breakdown of challenges addressed in this demonstration.

- Develop a backend application that interfaces with an LLM (done)
- Ensure the application can receive user prompts and forward them to the chosen LLM (done)
- Implement appropriate error handling and response formatting (in progress)
- Integrate the application with at least one LLM (done)
- Retrieval Augmented Generation (done)
- GUI (pending)
- Unit testing (pending)

