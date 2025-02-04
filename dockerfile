FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt update && apt install -y \
    python3.12 python3.12-dev python3-pip \
    libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev \
    build-essential libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev \
    libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev \
    && apt clean && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1 \
    && update-alternatives --config python3

RUN pip3 install --upgrade pip
