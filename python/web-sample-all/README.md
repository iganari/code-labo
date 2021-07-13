# Web Sample all

## Docker コンテナを用いて開発する時

```
cd code-labo/python/web-sample-all
```

+ コンテナの作成

```
docker build . --tag codelabo-py-websampleall
```

+ コンテナをデーモン起動

```
docker run \
  -d \
  -p 8080:5000 \
  -v $(pwd):/app \
  --name codelabo-py-websampleall \
  codelabo-py-websampleall
```

+ Web ブラウザから確認

http://0.0.0.0:8080

![](./01.png)

http://0.0.0.0:8080/healthz

![](./02.png)

http://0.0.0.0:8080/hogehoge

![](./03.png)

+ [debug] コンテナにログイン ---> :whale:

```
docker exec -it codelabo-py-websampleall /bin/bash
```

+ コンテナの作り直し OR 削除

```
docker stop codelabo-py-websampleall && \
docker rm -f codelabo-py-websampleall && \
docker rmi codelabo-py-websampleall
```
