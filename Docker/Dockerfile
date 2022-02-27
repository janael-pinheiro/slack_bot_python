FROM python:3.9.10-alpine

WORKDIR /app

COPY src src
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8080

ARG SLACK_TOKEN

#Update PYTHONPATH with the application folder
ENV PYTHONPATH=$PYTHONPATH:/app
ENV SLACK_TOKEN=$SLACK_TOKEN

CMD ["python3", "src/service/application.py"]
