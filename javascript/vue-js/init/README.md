# Vue.js

## Docker Compose を使って、コンテナを起動

+ Docker Compose の起動

```
docker-compose up -d
```

+ ステータスの確認

```
docker-compose ps
```

+ コンテナにログイン ---> :while:

```
docker exec -it codelab-vue-init /bin/sh
```


```
npm list vue
vue -V
```



+ :while: Vue.jsプロジェクトを作成
  + `Vue2` か `Vue3` と聞かれるので、 `Vue3` と答える 

```
vue create my-project
```


## Vue.js のプロジェクトの初期設定

```
cd my-project/
```

```
$ cd my-project
$ yarn serve
```


```
cat << __EOF__ > .env.local
NODE_ENV=local
VUE_APP_TITLE='My Staging App'
VUE_APP_PORT='9000'
VUE_APP_HOST='0.0.0.0'
PORT='9000'
HOST='0.0.0.0'
__EOF__
```
```
cat << __EOF__ > .env.development
NODE_ENV=development
__EOF__
```
```
cat << __EOF__ > .env.production
NODE_ENV=production
__EOF__
```


+ packace.json に加筆

```
"scripts": {
    "serve": "vue-cli-service serve",
    "local-serve": "vue-cli-service serve --mode local",
    "dev-serve": "vue-cli-service serve --mode development",
    "prod-serve": "vue-cli-service serve --mode production",
    "dev-build": "vue-cli-service build --mode development",
    "prod-build": "vue-cli-service build --mode production",
  }
```
```
yarn local-serve
yarn dev-serve
```

```
PORT=9000 yarn serve
```

+ Web ブラウザで確認

```
http://localhost:9000/
```

```
参考
https://zenn.dev/tet0h/articles/docker-vuejs
https://qiita.com/go6887/items/2e254d31b5a4af42f813
```


## 削除

```
docker-compose stop
docker-compose rm -f
```
