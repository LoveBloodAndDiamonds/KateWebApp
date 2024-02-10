# KateWebApp

Веб приложение с формой для ввода данных. В приложении присутствует функционал для отправки сообщений на почту и
телеграм.

# Инструкция по установке:

Подключиться к серверу:
```shell
ssh root@<ip>
```

### Обновление пакетов сервера
```shell
sudo apt update & sudo apt upgrade
```
```shell
apt install python3-pip
```

### Установка MySQL
```shell
sudo apt install mysql-server
```
```shell
sudo mysql
```
```sql
CREATE USER 'kate'@'localhost' IDENTIFIED BY 'kate';
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
```sql
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost' WITH GRANT OPTION;
```
```sql
FLUSH PRIVILEGES;
```
```sql
EXIT;
```

### Установка программы
```shell
git clone https://github.com/LoveBloodAndDiamonds/KateWebApp.git
```

### Как запускать и перезапускать программу после установки
```shell
mv kate_web_app.service /etc/systemd/system/
```
```shell
sudo systemctl daemon-reload
```
```shell
sudo systemctl start kate_web_app
```
```shell
sudo systemctl enable kate_web_app
```
```shell
systemctl status kate_web_app
```

### Как зайти в интерактивную оболочку MySQL
```shell
mysql -u kate -p
```

# Инструкция по работе с базой данных
Зайти в интерактивную оболочку mysql:
```shell
mysql
```

Перед началом работы обязательно надо указать с какой базой данных идет работа:
```sql
USE kate_database;
```

Просмотреть всю таблицу:
```sql
SELECT * FROM kate_database;
```

Выбрать только те строчки, где saw_dog=True
```sql
SELECT * FROM kate_database WHERE saw_dog=1;
```

Выйти из интерактивной оболочки
```sql
exit
```

# Как перезапустить программу с очисткой базы данных
```shell
sudo systemctl restart kate_web_app
```