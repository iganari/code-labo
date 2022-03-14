# large number of records

## 概要

WIP

## やってみる

```
cd code-labo/mysql/large-number-records
```

## Docker Compose で起動


```
docker-compose up -d --build
```
```
docker-compose ps
```


## ログイン

+ コンテナにログイン ---> :whale: 

```
docker-compose exec code-labo-mysql-large-num-records /bin/bash
```

## ソースコードの取得


+ :whale: MySQL の公式ページからサンプルをダウンロードする ( https://dev.mysql.com/doc/index-other.html )

```
cd /mnt

wget https://downloads.mysql.com/docs/world-db.zip
wget https://downloads.mysql.com/docs/world_x-db.zip
```

```
unzip world-db.zip
```


## サンプルデータを MySQL にいれる

+ サンプルデータを入れる

```
mysql -uroot -p < world-db/world.sql
```

+ ログイン

```
mysql -uroot -p
```



```
use world;
SELECT count(ID) from city;
```


```
### 例

mysql> SELECT count(ID) from city;
+-----------+
| count(ID) |
+-----------+
|      4079 |
+-----------+
1 row in set (0.01 sec)

```

+ 増やす

```
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;

---> 4079 * 2 = 8158 になるはず
```
```
### 例

mysql> SELECT count(ID) from city;
+-----------+
| count(ID) |
+-----------+
|      8158 |
+-----------+
1 row in set (0.00 sec)

---> 意図通りの数値になった :)
```

+ どんどん増やしていく

```
### 8,158 -> 16,316
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;

### 16,316 -> 32,632
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;

### 32,632 -> 65,264
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;

### 65,264 -> 130,528
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;

### 130,528 -> 261,056
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;

### 261,056 -> 522,112
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;

### 522,112 -> 1,044,224 == 100万レコード
INSERT INTO city SELECT 0, Name, CountryCode, District, Population FROM city;
```

+ 確認

```
mysql> SELECT count(ID) from city;
+-----------+
| count(ID) |
+-----------+
|   1044224 |
+-----------+
1 row in set (0.11 sec)

mysql> exit
Bye
```

## 抽出

+ mysqldump を用いて、抽出する

```
mysqldump -uroot -p world > world-large-number-records.sql
```

+ 確認

```
ls | grep world-large-number-records.sql
du -m world-large-number-records.sql
```
```
# ls | grep world-large-number-records.sql
world-large-number-records.sql

# du -m world-large-number-records.sql
47      world-large-number-records.sql

---> 47 MB のファイル
```

## 削除

```
docker-compose stop
docker-compose rm -f
```