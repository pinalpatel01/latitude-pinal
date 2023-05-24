# Install the python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the working directory
COPY . .

# Run the script
CMD ["python", "generate_anonymized_data.py"]
