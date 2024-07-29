# Use a Python base image
FROM python:latest

# Set the working directory inside the container
WORKDIR /myapp

# Copy the application code and directories with Excel files into the container
COPY . .

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Define the default command to run the script
CMD ["python3", "excel_combine.py"]
