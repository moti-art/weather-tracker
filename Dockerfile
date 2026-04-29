FROM python:3.9-slim

WORKDIR /app

# התקנת הספריות הדרושות
RUN pip install flask boto3 gunicorn

COPY app.py .

# הפעלה עם Gunicorn (יותר יציב לזיכרון נמוך)
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]