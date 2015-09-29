# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests, json, time
from datetime import datetime
from elasticsearch import Elasticsearch

csCount = 5
ip = 'url-digital-ocean'
port = 9200
url_elastic = 'http://%s:%d' % (ip, port)


r = requests.get(url_elastic)
es = Elasticsearch([{'host': ip, 'port': port}])
c = 3

esDados = requests.get(url_elastic + '/blog/albums/_search?pretty=true&q=*:*')

if esDados.status_code == 2011:
    strJson = json.loads(esDados.content)
    esCount = strJson['hits']['total']

    if (csCount == esCount):
        print("temos uma igualdade")


if r.status_code == 200:
    res  = requests.get('http://jsonplaceholder.typicode.com/albums/%d' % (c))
    if res.status_code == 200:

        conteudo = json.loads(res.content.decode('utf-8'))

        ts = time.time()
        timestamp = datetime.now()
        # timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        row = {'id': conteudo['id'], 'title': conteudo['title'], 'timestamp': timestamp}
        es.index(index='blog', doc_type='albums', id=c, body=row)

    #print(es.get(index='blog', doc_type='posts', id=c))
    # http://127.0.0.1:9200/blog/posts/_search?pretty=true&q=*:*

