# base image
FROM python:3.11-alpine

# working dir
WORKDIR /app

#copy the code 
COPY . /app

#required libraires
RUN pip install Flask

#run the code
CMD ["python", "app.py"]
