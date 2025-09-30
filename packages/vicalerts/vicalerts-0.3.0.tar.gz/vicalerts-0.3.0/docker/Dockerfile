FROM python:3.12-slim

# Install uv
RUN pip install --no-cache-dir uv

# Install vicalerts using uv
RUN uv pip install --system vicalerts

# Create a non-root user
RUN useradd -m -u 1000 vicalerts

# Set working directory
WORKDIR /app

# Switch to non-root user
USER vicalerts

# Copy healthcheck script
COPY healthcheck.py /healthcheck.py

# Run vicalerts run with database in mounted volume, polling every 60 seconds (recommended)
CMD ["vicalerts", "run", "--db", "/data/vicalerts.db", "--no-progress", "--interval", "60"]