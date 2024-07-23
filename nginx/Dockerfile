# 使用官方的 Nginx 镜像作为基础镜像
FROM nginx:latest

# 创建目录用于存放证书
RUN mkdir -p /etc/nginx/certs

# 复制证书文件到容器内部
#COPY certs/nantong.titi365.com.pem /etc/nginx/certs/nantong.titi365.com.pem
#COPY certs/nantong.titi365.com.key /etc/nginx/certs/nantong.titi365.com.key

#RUN rm /etc/nginx/conf.d/default.conf
#COPY ./nginx.conf /etc/nginx/conf.d/

#RUN rm /etc/apt/sources.list.d/* -f
#ADD ./sources.list /etc/apt
#RUN apt-get update && apt-get install -y --no-install-recommends gcc iputils-ping