FROM python:3.10.13-slim as base

WORKDIR /app

# Copy the source code into the container.
COPY . .

RUN pip install -r requirements.txt

# Run the application. 'myenv.Lib.site-packages.werkzeug.wsgi'
CMD gunicorn --bind=0.0.0.0:5000 wsgi:app
