FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "docker/entrypoint.sh"]