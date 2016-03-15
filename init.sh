sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
#sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.conf
sudo /etc/init.d/gunicorn restart
#sudo gunicorn -b 0.0.0.0:8080 hello
#sudo ln -sf /home/box/web/hello.py /usr/local/lib/python2.7/hello.py
#sudo rm /etc/gunicorn.d/hello.conf

