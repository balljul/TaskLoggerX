# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./src/requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ./src /app/

# Set environment variables if needed
ENV DB_HOST=mysql
ENV DB_PORT=3306
# ... other environment variables

# Command to run your Python application
CMD ["python", "main.py"]
