import json

import boto3


class BedrockService(object):
    """
    Interface to an AWS Bedrock foundational model
    """
    def __init__(self,
                 aws_access_key_id: str,
                 aws_secret_access_key: str,
                 region: str):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region = region
        self.session = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )
        self.client = self.session.client(
            service_name="bedrock",
            region_name=self.region
        )
        self.runtime = self.session.client(
            service_name="bedrock-runtime",
            region_name=self.region
        )
        self.model_kwargs = {
            "modelId": "ai21.j2-ultra-v1",
            "contentType": "application/json",
            "accept": "*/*"
        }

    def make_body(self, prompt: str) -> str:
        """
        Using the given prompt, build the json body required for prompting this
        model.
        """
        return json.dumps({
            "prompt": prompt,
            "maxTokens": 200,
            "temperature": 0.7,
            "topP": 1,
            "stopSequences": [],
            "countPenalty": {"scale": 0},
            "presencePenalty": {"scale": 0},
            "frequencyPenalty": {"scale": 0}
        })

    def prompt(self, prompt: str) -> str:
        """
        Prompt the model and parse out the reply, which is nested deep inside
        the reponse.
        """
        response = self.runtime.invoke_model(
            body=self.make_body(prompt),
            **self.model_kwargs
        )
        output = json.loads(response.get("body").read())
        return output.get("completions")[0].get("data").get("text")
