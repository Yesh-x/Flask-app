FROM python:3.8-slim-buster
 
WORKDIR /app
 
COPY . /app
 
RUN pip install --no-cache-dir Flask
 
EXPOSE 3000
 
CMD ["python", "app.py"]
