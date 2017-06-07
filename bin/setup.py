#!/usr/bin/python
from os import system, listdir
from webbrowser import open

def main():
	try:
		files = listdir(".")
		for i in files:
			if i == "manage.py":
				system("python manage.py migrate")
				system("python manage.py makemigrations salt")
				system("python manage.py migrate")
				open("http://localhost:2000")
				system("python manage.py runserver 2000")
				quit()
				break
		system("python ../manage.py migrate")
		system("python ../manage.py makemigrations salt")
		system("python ../manage.py migrate")
		open("http://localhost:2000")
		system("python ../manage.py runserver 2000")
	except Exception as exp:
		print("Something went wrong!")
		print("Details : \n")
		print(exp)
		quit()

if __name__ == '__main__':
	main()
