FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install flask
CMD ["python", "app/app.py"]

