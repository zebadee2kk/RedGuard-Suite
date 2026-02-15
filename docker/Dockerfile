FROM python:3.12-slim AS base

LABEL maintainer="RedGuard Contributors"
LABEL description="RedGuard Suite - Ethical Red Teaming Framework"

# Security: run as non-root
RUN groupadd -r redguard && useradd -r -g redguard -d /app -s /sbin/nologin redguard

WORKDIR /app

# Install system dependencies for security tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    nmap \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml .
COPY src/ src/
RUN pip install --no-cache-dir .

# Copy configs and docs
COPY configs/ configs/
COPY docs/ docs/

# Drop privileges
USER redguard

ENTRYPOINT ["redguard"]
CMD ["--help"]
