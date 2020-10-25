FROM python:3.6.1-alpine
RUN pip install flask
COPY algo-fibo.py /algo-fibo.py
CMD ["python","algo-fibo.py"]
