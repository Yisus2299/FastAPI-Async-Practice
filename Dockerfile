FROM python:3.12-slim

WORKDIR /app

# COPY ALL REQUIREMENTS AND INSTALL
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY THE CODE
COPY . .

# EXPOSE THE PORT
EXPOSE 8000

# COMMAND TO RUN IT
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]