# Use the official Python image as a base image
FROM python:latest

# Set the working directory in the container
WORKDIR /usr/app/src

# Copy the requirements file into the container
COPY app/requirements.txt /app/src/

# # Install the Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app/main.py ./

# Command to run your Python application
CMD ["python", "main.py"]