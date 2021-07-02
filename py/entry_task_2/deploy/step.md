# 定时任务启动
python manage.py celery worker --loglevel=info

# 启动NG
brew services start nginx

# 启动gunicorn
gunicorn -c startup/gunicorn.py startup.wsgi:application

# 关闭
ps -ef|grep gunicorn  / kill #pid
