# استفاده از ایمیج رسمی پایتون
FROM python:3.9-slim

# تنظیم دایرکتوری کاری در کانتینر
WORKDIR /code

# نصب وابستگی‌ها
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن فایل‌های پروژه به کانتینر
COPY . /code/

# باز کردن پورت 8000 برای جنگو
EXPOSE 8000

# اجرای سرور توسعه جنگو
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]