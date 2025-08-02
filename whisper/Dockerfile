FROM python:3.10-slim

# Install system dependencies (ffmpeg is required by openai-whisper)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Create application directory
WORKDIR /app

# Copy dependency definitions
COPY requirements.txt ./

# Install Python dependencies. 
# --no-cache-dir helps keep the image size down by not storing wheels.
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY transcribe.py ./transcribe.py

# Set the default command. When run without arguments, the container will show usage info.
CMD ["python", "./transcribe.py", "--help"]