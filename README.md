# ChatGPT Line Bot

## 功能

> ChatGPT

## 建置

> 複製 `settings.example.py` 為 `settings.py`，並修改環境變數

### 開發環境

```bash
pipenv install
pipenv run python manage.py runserver
```

### Docker 部署

```bash
# 啟動 Docker container
make up

# 停止並移除 Docker container
make down
```

#### Docker image

```bash
# 建立 image
make build

# 刪除 image
make rm

# 重建 image
make rebuild
```

#### Docker container

```bash
# 執行 container
make run

# 停止 container
make stop

# 查看 container 日誌
make logs

# 查看 container 日誌
make exec

# 重啟 container
make restart
```
