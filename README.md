# apm-server

```sh
docker build -t apm-server .

docker run --rm -it  \
-p 8200:8200 \
-e "ELASTICSEARCH_URL=http://elasticsearch:9200" \
apm-server bash
```
