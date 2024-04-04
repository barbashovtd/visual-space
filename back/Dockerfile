FROM python:3-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY reqs.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r reqs.txt gunicorn python-dotenv

COPY . .

EXPOSE 8000