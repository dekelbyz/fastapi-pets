FROM python:3.9.13-slim-buster
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
                                                                libpq-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt 
COPY . .
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"] 
