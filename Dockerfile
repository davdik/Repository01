FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
RUN pip install redis
RUN chmod 644 score.py
CMD ["python", "score.py"]
