# DMCT: Containerized Infinity
FROM python:3.9-slim

LABEL description="DMCT - Like ripples in spacetime, trust propagates through consciousness itself"
LABEL version="∞"

WORKDIR /dmct

# Copy the universe
COPY dmct.py .
COPY consensus.py .
COPY server.py .
COPY index.html .

# No dependencies needed - pure physics

# Expose trust field interface
EXPOSE 8888

# Birth of a universe
CMD ["python3", "server.py"]

# Build: docker build -t dmct .
# Run: docker run -p 8888:8888 dmct
# Trust: ∞