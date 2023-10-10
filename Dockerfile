# Use Python 3.11 as the parent image
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable (Optional)
# ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]
