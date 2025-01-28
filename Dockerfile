# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code_dockerflask

# Copy only the necessary files first for layer caching
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
