# Saltan
By @mentix02

![](http://imageshack.com/a/img922/530/8n2tqG.png)

A simple __Django__ powered image board.

Registered users can upload images with some description and other registered users can talk about them.

### Frameworks used
+ Django
+ Bootstrap
+ jQuery

### Languages
+ Python
+ HTML5
+ JavaScript (jQuery)
+ SCSS

### Contribute
To get started with developing Saltan, run in terminal -

_make sure you have a MySQL database called __Saltan__ created!_
```sh
git clone https://github.com/mentix02/Saltan.git
cd Saltan/
sudo pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations salt
python manage.py migrate
python manage.py runserver
```
And you're done! Enjoy!

__OR__

After having a MySQL database called __Saltan__ created just run -
```sh
python setup.py
```
Powered by Django.
