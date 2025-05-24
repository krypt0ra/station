FROM python:3.13
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/TA-Lib/ta-lib/releases/download/v0.6.3/ta-lib-0.6.3-src.tar.gz && \
    tar -xvzf ta-lib-0.6.3-src.tar.gz && \
    cd ta-lib-0.6.3 && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cd .. && rm -rf ta-lib*

COPY .. .

RUN pip install --upgrade pip
RUN pip install -r app/requirements-step-1.txt --no-cache-dir --root-user-action=ignore
RUN pip install -r app/requirements-step-2.txt --no-cache-dir --root-user-action=ignore

CMD ["tail", "-f", "/dev/null"]

