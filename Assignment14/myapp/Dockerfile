# Step 1: Start with a base image
FROM python:3.8-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy all files from the current directory to the container's /app directory
COPY . /app

# Step 4: Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Run the app (replace app.py with your main script)
CMD ["python", "app.py"]

