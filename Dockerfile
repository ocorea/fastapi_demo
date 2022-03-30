FROM python:3.9-slim
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#execute command
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
