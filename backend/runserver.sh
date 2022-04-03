#!/bin/bash
ip=127.0.0.1
port=8080
exec python3 manage.py runserver $ip:$port
