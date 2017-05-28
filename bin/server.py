#!/usr/bin/python
from os import system, listdir


def main():
	try:
		files = listdir(".")
		for i in files:
			if i == "manage.py":
				print("Starting server...")
				system("python manage.py runserver 2000")
				quit()
				break
		system("python ../manage.py runserver 2000")
	except Exception as exp:
		print("Something went wrong!")
		print("Details : \n")
		print(exp)
		quit()

if __name__ == '__main__':
	main()
