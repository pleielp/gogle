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
