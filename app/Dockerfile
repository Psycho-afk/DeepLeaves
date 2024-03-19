FROM python:3.10.13-slim as base

WORKDIR /app

# Copy the source code into the container.
COPY . .

# Upgrade pip first
RUN pip install --upgrade pip


RUN pip install -r requirements.txt 

EXPOSE 5000

# Run the application. 'myenv.Lib.site-packages.werkzeug.wsgi'
CMD flask run app gunicorn --bind=0.0.0.0:5000 wsgi:app

#-------------------------------- 