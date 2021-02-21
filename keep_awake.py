#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import requests


def ping():
    # requests.get('https://felippe-notion-server.herokuapp.com/')
    requests.get('http://127.0.0.1:8000/')
