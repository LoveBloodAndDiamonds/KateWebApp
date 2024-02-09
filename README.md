# KateWebApp

Веб приложение с формой для ввода данных. В приложении присутствует функционал для отправки сообщений на почту и
телеграм.

## Инструкция по установке:

### Обновление пакетов сервера
```shell
sudo apt update & sudo apt upgrade
```

### Установка MySQL
```shell
sudo apt install mysql-server
```
```shell
sudo mysql_secure_installation
```
```shell
sudo mysql
```
```sql
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
Далее нужно запустить программу через .service

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