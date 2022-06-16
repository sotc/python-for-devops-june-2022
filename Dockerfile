FROM python:3.8.13-slim-buster

RUN mkdir -p /app
COPY . wikisearch.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 8080
CMD [ "wikisearch.py" ]
ENTRYPOINT [ "python" ]