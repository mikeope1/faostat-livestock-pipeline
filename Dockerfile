FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py queries.sql ./
CMD ["sh", "-c", "python transform.py && python load.py && python run_queries.py"]