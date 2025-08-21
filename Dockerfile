FROM python:3.13.7-slim
WORKDIR /code
COPY app.py requirements.txt  /code/
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "4"]