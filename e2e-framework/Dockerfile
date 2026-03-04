FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

WORKDIR /app

# ===== SYSTEM DEPS =====
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# ===== PYTHON DEPS =====
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ===== PROJECT FILES =====
COPY . .

# ===== ENTRYPOINT =====
ENTRYPOINT ["bash", "entrypoint.sh"]