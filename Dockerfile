FROM python:3-slim

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

ADD requirements.txt .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN python -m pip install tweepy
RUN apt install -y mecab libmecab-dev mecab-ipadic-utf8 swig
RUN pip install -r requirements.txt