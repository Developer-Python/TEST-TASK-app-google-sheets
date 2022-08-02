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

### 2) Настройка БД | PostgreSql == 14.4

- Потребуется установить - `PostgreSql` 
- https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- Заходим в директорию с установленной - `PostgreSql` у меня это `C:\Program Files\PostgreSQL` 
- Открываем `cmd` или `ConEmu` и в самой консоли переходим в `C:\Program Files\PostgreSQL\14\bin` и прописываем следующее:
1) `psql.exe -U postgres` или `psql.exe` | У вас запросит пароль, ввидите который создавали при установке `PostgreSql`
2) Терминал изменится на `postgres=#` далее:
3) `CREATE DATABASE sheets;`
4) `CREATE USER admin WITH ENCRYPTED PASSWORD 'admin'; `
5) `ALTER ROLE admin SET client_encoding TO 'utf8';`
6) `ALTER ROLE admin SET default_transaction_isolation TO 'read committed';`
7) `ALTER ROLE admin SET timezone TO 'UTC';`
8) `GRANT ALL PRIVILEGES ON DATABASE sheets TO admin;`

----------------------------------------------
### 3) Настройка Админки и БД | Django == 3.0

- Открываем `cmd` или `ConEmu` и в самой консоли переходим в `\app-google-sheets` там будет файл manage.py, прописываем следующее:
1) `django-admin createsuperuser` - Создаёте супер пользователя(Имя: admin, Почта: пропуск, Пароль: admin, Повторный пароль: admin)
2) `python manage.py migrate` - Применяем миграцию, так как у нас новая БД
3) `python manage.py runserver` - Запускаете сервер и переходите на `127.0.0.1:8000`
4) `127.0.0.1:8000/admin` - Можете зайти в админку(по желанию)
