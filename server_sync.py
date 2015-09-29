# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests, json, time
from datetime import datetime
from elasticsearch import Elasticsearch



class ServerSync:
    def __init__(self, params):
        self.es_url = params['elasticsearch']
        pass

    def check_server(self):




ss = ServerSync()
ss.check_server()

