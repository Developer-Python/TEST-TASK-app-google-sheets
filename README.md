# PROJECT - currency-handler

### Внимание! Очень важно точно проделывать все ниже написанные инструкций для корректной работы проекта:

----------------------------------------------

### 1) Настройка пакетов | Python == 3.8.0

1) pip3 install django3.0
2) pip3 install django-grappelli
3) pip3 install jsonfield
4) pip3 install requests
5) pip3 install google-api-python-client
6) pip3 install google-auth 
7) pip3 install google-auth-httplib2 
8) pip3 install httplib2 
9) pip3 install oauth2client
10) pip3 install psycopg2
11) pip3 install bs4
12) pip3 install lxml

----------------------------------------------

### 2) PostgreSql 

- Потребуется установить ПО - `PostgreSql` 
- Заходим в директорию с установленной - `PostgreSql` у меня это `C:\Program Files\PostgreSQL` 
- Открываем `cmd` или `ConEmu` в консоли переходим в `C:\Program Files\PostgreSQL\14\bin` и прописываем следующее:
1) `psql.exe -U postgres` или `psql.exe` | Вам надо войти в аккаунт, чтобы получить доступ!
- Терминал изменится на `postgres=#` далее:
2) `CREATE DATABASE sheets;`
3) `CREATE USER admin WITH ENCRYPTED PASSWORD 'admin'; `
4) `ALTER ROLE admin SET client_encoding TO 'utf8';`
5) `ALTER ROLE admin SET default_transaction_isolation TO 'read committed';`
6) `ALTER ROLE admin SET timezone TO 'UTC';`
7) `GRANT ALL PRIVILEGES ON DATABASE sheets TO admin;`
