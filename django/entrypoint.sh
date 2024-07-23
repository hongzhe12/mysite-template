# entrypoint.sh
#!/bin/bash

# 等待数据库服务启动（可选）
# ./wait-for-it.sh postgres:5432 --

# 执行数据库迁移
python manage.py migrate

# 启动 Django 服务
exec uvicorn app.asgi:application --host 0.0.0.0 --port 8000 --workers 10
