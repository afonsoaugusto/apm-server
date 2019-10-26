#!/bin/bash

python3 render.py

mv /templates/apm-server.yml /etc/apm-server/apm-server.yml

apm-server run