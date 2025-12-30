FROM python:latest

WORKDIR /workspace

RUN apt-get update

# pipのアップデート
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ポート5000を公開
# EXPOSE 5000

# サーバーを起動
# CMD ["python", "src/api.py"]