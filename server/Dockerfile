FROM python:3.9.6-slim-buster

ENV APP_DIR=/opt/app

SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && mkdir -p /usr/share/man/man1 \
    && apt-get install --no-install-recommends -qq -y \
        build-essential \
        gosu \
        libpcre3 \
        libpcre3-dev \
        curl \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_DIR}
COPY openapi_server openapi_server/
RUN mkdir dslim-bert
COPY requirements.txt prod-requirements.txt uwsgi.ini ./

#download dslim-bert model
RUN mkdir dslim-bert/model \
    && mkdir dslim-bert/tokenizer \
    && curl -O https://huggingface.co/dslim/bert-base-NER/blob/main/config.json \
    && curl -O https://huggingface.co/dslim/bert-base-NER/blob/main/pytorch_model.bin \
    && mv config.json dslim-bert/model \
    && mv pytorch_model.bin dslim-bert/model \
    && curl -O https://huggingface.co/dslim/bert-base-NER/blob/main/special_tokens_map.json \
    && curl -O https://huggingface.co/dslim/bert-base-NER/blob/main/tokenizer_config.json \
    && curl -O https://huggingface.co/dslim/bert-base-NER/blob/main/vocab.txt \
    && mv special_tokens_map.json dslim-bert/tokenizer \
    && mv tokenizer_config.json dslim-bert/tokenizer \
    && mv vocab.txt dslim-bert/tokenizer \
#install requirements    
    && pip install --no-cache-dir \
    -r requirements.txt -r prod-requirements.txt \
    && useradd --create-home --shell /bin/bash nlp 


WORKDIR /
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

EXPOSE 8080

RUN echo 'uwsgi_read_timeout 300s > /etc/nginx/conf.d/custom_timeout.conf'

ENTRYPOINT ["/docker-entrypoint.sh"]

# Run server in development mode
# CMD ["python", "-m", "openapi_server"]

# Run server in production mode
CMD ["uwsgi", "--ini", "uwsgi.ini", "--lazy", "--http", ":8080"]