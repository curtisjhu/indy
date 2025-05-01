# Use the official Python 11 image as the base image
FROM python:11-slim

# Set the working directory inside the container
WORKDIR /engine

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on (if applicable)
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]