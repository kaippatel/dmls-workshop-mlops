FROM python:3.12-slim

# Set working directory 
WORKDIR /app

# Install dependencies 
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy code 
COPY . .

# Run FastAPI app with Uvicorn
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]