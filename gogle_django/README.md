# With Django

# for changing to Mysql

### MYSQL

```
create user 'gogle'@'localhost' identified by 'gogle'
grant all privileges on *.* to 'gogle'@'localhost';
```

### DJANGO (in config/settings.py)

`pip install mysqlclient`

> [Django DB Connection Reference](https://docs.djangoproject.com/en/2.2/ref/databases/#connecting-to-the-database)

### Quick Start

1. `source env/bin/activate/`
2. `pip install -r requirement.txt`
3. Go to `cd gogle/gogle_django`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python test.py` just wait 10 second!! and `ctrl + c`!! (crawling so many data)
7. make super user for login admin site `python manange.py createsuperuser`
8. run django server for checking data `python manage.py runserver`
9. Finish.
