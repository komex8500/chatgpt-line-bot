# 使用 Python 官方的基礎映像
FROM python:3.11-slim

WORKDIR /code

# 安裝依賴
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Pipenv
RUN pip install pipenv

# 複製 Pipfile 和 Pipfile.lock 到容器內的工作目錄
COPY Pipfile Pipfile.lock /code/

# 安装 Python 依赖
RUN pipenv install --system --deploy --ignore-pipfile

# 複製專案程式碼到容器內的工作目錄
COPY . /code/

# 定義容器執行的預設指令
CMD python manage.py runserver 0.0.0.0:8000