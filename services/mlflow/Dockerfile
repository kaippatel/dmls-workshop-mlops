FROM python:3.12-slim

WORKDIR /app

RUN python -m pip install --upgrade pip && \
    pip install "mlflow==3.2.0"

# Run MLflow server
EXPOSE 5000
CMD ["mlflow", "server", \
     "--host", "0.0.0.0",\
     "--port", "5000", \
     "--backend-store-uri", "sqlite:////mlflow/mlflow.db", \
     "--serve-artifacts", \
     "--artifacts-destination", "/mlruns"]