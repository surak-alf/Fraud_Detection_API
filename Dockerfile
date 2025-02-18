FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r api/requirements.txt # Corrected path

EXPOSE 5000

CMD ["python", "api/serve_model.py"]