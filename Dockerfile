# 1. Use an official Python base image
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy your application code into the container
COPY . /app

# 4. Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port Flask will run on
EXPOSE 8080

# 7. Run Flask
CMD ["python3", "main_api.py"]
