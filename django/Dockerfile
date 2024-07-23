###########
# BUILDER #
###########

# pull official base image
FROM python:3.9-slim-bullseye AS builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
ADD ./sources.list /etc/apt
RUN apt-get update && apt-get install -y gcc

# lint
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN pip install flake8==6.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /usr/src/app/
# RUN flake8 --ignore=E501,F401 .  # 静态代码检查

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt \
    -i https://pypi.tuna.tsinghua.edu.cn/simple


#########
# FINAL #
#########

# pull official base image
FROM python:3.9-slim-bullseye

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/django
RUN mkdir $APP_HOME
RUN bash -c "mkdir -p $APP_HOME/{logs,static,media}"
WORKDIR $APP_HOME

# install dependencies
ADD ./sources.list /etc/apt
RUN apt-get update && apt-get install -y --no-install-recommends gcc netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache /wheels/* -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制启动脚本
COPY entrypoint.sh /home/app/django/entrypoint.sh
RUN chmod +x /home/app/django/entrypoint.sh

# chown all the files to the app user
RUN chown -R app:app $HOME

# change to the app user
USER app


