FROM public.ecr.aws/lambda/python:3.12

COPY ./tweeteval/app.py ./tweeteval/requirements.txt ./
RUN python3 -m pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

COPY ./tweeteval ${LAMBDA_TASK_ROOT}/

CMD [ "app.lambda_handler" ]