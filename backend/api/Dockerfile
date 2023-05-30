# Use the official Python base image with the desired version
FROM python:3.10

# Set environment variables for Python buffering and ensuring stdout/stderr are not buffered
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the Django project code to the container
COPY . .

# Expose the port on which the Django app will run (adjust if necessary)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
