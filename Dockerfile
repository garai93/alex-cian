FROM mcr.microsoft.com/playwright/python:v1.43.0

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x entrypoint.sh

CMD ["bash", "entrypoint.sh"]
