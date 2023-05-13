# Use a Python base image
FROM python:3.9


RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point command to run the Flask application
CMD ["python", "main.py"]
