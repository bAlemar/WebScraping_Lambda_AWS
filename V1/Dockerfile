FROM public.ecr.aws/lambda/python:3.10

COPY ./ ${LAMBDA_TASK_ROOT}

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["main.handler"]