FROM python:3.10-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Default run
CMD ["python","app.py"]

# Test stage 
FROM base AS test
CMD ["pytest","-v"]
