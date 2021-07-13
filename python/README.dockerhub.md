# Code Labo Python

## 概要

Flask を使ったサンプル Web コンテナ

## 使いかた

```
docker run \
  --rm \
  -p 8080:5000 \
  --name code-labo-python \
  iganarix/code-labo-python
```

+ Web ブラウザから確認

http://0.0.0.0:8080

![](https://raw.githubusercontent.com/iganari/code-labo/modify-readme-only/python/web-sample-all/01.png)

http://0.0.0.0:8080/healthz

![](https://raw.githubusercontent.com/iganari/code-labo/modify-readme-only/python/web-sample-all/02.png)

http://0.0.0.0:8080/hogehoge

![](https://raw.githubusercontent.com/iganari/code-labo/modify-readme-only/python/web-sample-all/03.png)
