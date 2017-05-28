#!/usr/bin/python
from os import system
import webbrowser

def main():
	system('python ../manage.py migrate')
	system('python ../manage.py makemigrations salt')
	system('python ../manage.py migrate')
	webbrowser.open('http://localhost:8000', 2)
	system('python ../manage.py runserver 2000')

if __name__ == '__main__':
	main()
