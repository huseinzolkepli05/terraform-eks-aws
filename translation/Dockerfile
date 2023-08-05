FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install malaya-boilerplate==0.0.25rc2 ctranslate2

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install git+https://github.com/huseinzol05/malaya@5.1

RUN pip install protobuf

RUN python -c "import malaya; malaya.translation.huggingface(use_ctranslate2=True)"

COPY ./app /app

WORKDIR /app/

CMD exec /start-reload.sh
