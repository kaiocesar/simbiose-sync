# -*- coding: utf-8 -*-

import requests, json, datetime, time
from elasticsearch import Elasticsearch

csCount = 3

r = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
c = 6

esDados = requests.get('http://127.0.0.1:9200/blog/albums/_search?pretty=true&q=*:*')

if esDados.status_code == 2011:
    strJson = json.loads(esDados.content)
    esCount = strJson['hits']['total']

    if (csCount == esCount):
        print("temos uma igualdade")


if r.status_code == 200:
    res  = requests.get('http://jsonplaceholder.typicode.com/albums/'  + str(c))
    if res.status_code == 200:
        conteudo = json.loads(res.content)

        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H-%M-%S")
        row = {'id': conteudo['id'], 'title': conteudo['title'], 'timestamp':timestamp}
        es.index(index='blog', doc_type='albums', id=c, body=row)
    #print(es.get(index='blog', doc_type='posts', id=c))
    # http://127.0.0.1:9200/blog/posts/_search?pretty=true&q=*:*

