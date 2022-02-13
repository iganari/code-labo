# Python: Web SubProcess

## Docker コンテナを用いて開発する時

```
cd code-labo/python/web-subprocess
```

+ コンテナの作成

```
docker build . --tag codelabo-py-websubprocess
```

+ コンテナをデーモン起動

```
docker run \
  -d \
  -p 8080:5000 \
  -v $(pwd):/app \
  --name codelabo-py-websubprocess \
  codelabo-py-websubprocess
```

+ Web ブラウザから確認

http://0.0.0.0:8080

![](./01.gif)

+ [debug] コンテナにログイン ---> :whale:

```
docker exec -it codelabo-py-websubprocess /bin/bash
```

+ コンテナの作り直し OR 削除

```
docker stop codelabo-py-websubprocess && \
docker rm -f codelabo-py-websubprocess && \
docker rmi codelabo-py-websubprocess
```
