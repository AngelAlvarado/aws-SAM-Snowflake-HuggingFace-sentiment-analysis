# Deploying HuggingFace sentiment-analysis model using AWS SAM

Steps to deploy TweetEval model:

- run `python manually_download_model_before_deployment`
- Make sure SAM is configured correctly
- Make sure your AWS accout has the necesary permissions: it will use Lambda, ECS, ECR, AIM, S3
- `sam build`
- `sam deploy --resolve-image-repos`, or in case you use a profile `sam deploy --resolve-image-repos --profile mfa`
