sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "create database stepic_db"
#sudo mysql -uroot -e "CREATE USER 'box'@'localhost';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_db.* TO 'box'@'localhost' WITH GRANT OPTION;"

