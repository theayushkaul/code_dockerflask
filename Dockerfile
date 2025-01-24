# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code_dockerflask

# Copy the current directory's contents into the container
COPY . /code_dockerflask

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
