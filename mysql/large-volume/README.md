# large volume

## 概要

WIP

## やってみる

```
cd code-labo/mysql/large-volume
```

## Docker Compose で起動

+ Docker Compose 起動

```
docker-compose up -d --build
```
```
docker-compose ps
```


## ログイン

+ コンテナにログイン ---> :whale: 

```
docker-compose exec code-labo-mysql-large-volume /bin/bash
```

## サンプル画像の入手


+ :whale: サンプルを提供してるページからファイルダウンロードする ( https://sample-img.lb-product.com/ )

```
cd /mnt

wget https://sample-img.lb-product.com/wp-content/themes/hitchcock/images/100MB.png
```

```
du -h 100MB.png
```
```
### 例

# du -h 100MB.png
113M    100MB.png
```

## サンプルデータを MySQL にいれる

+ ログイン

```
mysql -uroot -p
```

+ `secure_file_priv` の確認

```
SHOW VARIABLES LIKE 'secure_file_priv';
```
```
### 例 ( NULL で無ければ OK )

mysql> SHOW VARIABLES LIKE 'secure_file_priv';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| secure_file_priv | /     |
+------------------+-------+
1 row in set (0.01 sec)

```

+ `max_allowed_packet` の確認

```
## mysql

SHOW VARIABLES like 'max_allowed_packet';
```
```
### 例

mysql> SHOW VARIABLES like 'max_allowed_packet';
+--------------------+-----------+
| Variable_name      | Value     |
+--------------------+-----------+
| max_allowed_packet | 157286400 |
+--------------------+-----------+
1 row in set (0.00 sec)

```

+ 諸々作成

```
## mysql

CREATE DATABASE large_volume;
USE large_volume;
```

```
## mysql

CREATE TABLE images (id int not null primary key auto_increment , image LONGBLOB);
```

```
## mysql

INSERT images values(0, LOAD_FILE('/mnt/100MB.png'));
```

+ もしくは `-c` を使ってみる( 0123456789abcd )

```
## Bash

mysql -uroot -p0123456789abcd large_volume -e "INSERT images values(0, LOAD_FILE('/mnt/100MB.png'));"
```

---> これでも出来るはず。これを何回かやり直す

## 抽出

+ 環境変数にいれる

```
export _mysql_root_passwd=$(cat docker-compose.yml | grep MYSQL_ROOT_PASSWORD | awk -F\: '{print $2}' | sed 's/\ //g')
```

+ mysqldump してデータを出してみる

```
mysqldump -uroot -p${_mysql_root_passwd} large_volume > large_volume.sql
```
```
# du -h large_volume.sql 
1001M   large_volume.sql
```

## さらに増やす

```
### 1G -> 2G
mysql -uroot -p${_mysql_root_passwd} large_volume -e "INSERT INTO images SELECT 0, image FROM images;"

### 2G -> 4G
mysql -uroot -p${_mysql_root_passwd} large_volume -e "INSERT INTO images SELECT 0, image FROM images;"

### 4G -> 8G
mysql -uroot -p${_mysql_root_passwd} large_volume -e "INSERT INTO images SELECT 0, image FROM images;"
```

```
mysqldump -uroot -p${_mysql_root_passwd} large_volume > large_volume.sql
```
```
# du -h large_volume.sql 
7.9G    large_volume.sql
```

## 削除

```
docker-compose stop
docker-compose rm -f
```