FROM python:3.7

# バッファの無効化と.pycの生成無効化
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /emitas
COPY Pipfile Pipfile.lock /emitas/

# --system:         仮想環境ではなくデフォルトのPythonにインストール
# --dev:            devパッケージもインストール
# --ignore-pipfile: pipfileではなく、pipfiile.lockを元にインストール？
# --deploy:         PipfileとPipfile.lock にズレがあるとき（pipenv syncし忘れた時）にエラーにする
RUN pip install pipenv && pipenv install --system --dev --ignore-pipfile --deploy
# pipenvのscriptを動かすために必要なコマンド これがないと、manage.py系のコマンドが動かなくなる
RUN pipenv install 

COPY . /emitas/
