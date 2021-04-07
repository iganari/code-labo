# Web Sample 01

## Docker コンテナを用いて開発する時

```
cd code-labo/python/web-sample-01
```

+ コンテナの作成

```
docker build . --tag codelabo-python-websample01
```

+ コンテナをデーモン起動

```
docker run \
  -d \
  -p 8080:5000 \
  -v $(pwd):/app \
  --name codelabo-python-websample01 \
  codelabo-python-websample01
```

+ Web ブラウザから確認

http://0.0.0.0:8080

+ [debug] コンテナにログイン ---> :whale:

```
docker exec -it codelabo-python-websample01 /bin/bash
```

+ コンテナの作り直し OR 削除

```
docker stop codelabo-python-websample01 && \
docker rm -f codelabo-python-websample01 && \
docker rmi codelabo-python-websample01
```
