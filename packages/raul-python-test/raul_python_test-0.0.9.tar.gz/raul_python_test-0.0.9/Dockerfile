FROM python:3.12-slim

WORKDIR /app

# Install git and clean up apt caches to keep the image small
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only dependency files first (for caching)
COPY pyproject.toml ./

# Copy the rest of your project
COPY . .

# Install build dependencies and your package (including runtime dependencies)
RUN pip install --no-cache-dir .

# Set the default command (replace 'app.py' with your entry point)
CMD ["raul-python-test"]
