## pyblog

### 非docker环境配置
```
# FLASK_ENV可自定义为: develop, testing, staging, product, default
yum install -y python36
pip install -r requirements.txt
export FLASK_ENV=develop
export MYSQL_HOST=192.168.19.12
export MYSQL_PORT=3306
export MYSQL_DATABASE=cicd
export MYSQL_USER=root
export MYSQL_PASSWORD=123456
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
python3 manage.py runserver -p 8003 -h 0.0.0.0 -d -r --threaded
```

### docker环境配置
```
# docker build image
docker build -t kevin163/pyblog:vbeta .
# docker create container
docker run -d -p 8003:8003 --name pyblog \
-e FLASK_ENV=develop \
-e MYSQL_HOST=192.168.19.12 \
-e MYSQL_PORT=30006 \
-e MYSQL_DATABASE=cicd \
-e MYSQL_USER=root \
-e MYSQL_PASSWORD=123456 \
kevin163/pyblog:vbeta
```
