FROM python:3.8-alpine
ADD score.py /
CMD ["python3.8", "./score.py"]
