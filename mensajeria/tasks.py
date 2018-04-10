from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
import json
import requests


@shared_task
def create_comment():
    for data_comment in extract_data_api():
        Comment.objects.create(**data_comment)


def extract_data_api():
    headers = {'Content-Type': 'application/json'}
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
