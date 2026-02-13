FROM python:3.10-slim-buster
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "bot.py"]
