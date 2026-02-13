# This bot is developed by **RETOUCH**
FROM python:3.10-slim-buster

WORKDIR /app
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

# EXPOSE THE STANDARD PORT
EXPOSE 8080

CMD ["python3", "bot.py"]
