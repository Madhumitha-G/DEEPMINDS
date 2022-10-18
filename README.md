# DEEPMINDS
Picture sharing website
DEEPMINDS
·        Group 6
We, the team DeepMinds , created a picture sharing project named Drop Box.
Main functionalities of our project :
·         It is picture sharing website among a community of people – currently runs on localhost / instructions to make it run on public web address is also given below 
·         The user can login / create an account to access the website
Features:
1.   	Upload pictures with hashtags
2.   	View pictures
3.   	Download pictures
4.   	Search a particular picture based on hashtags
5.   	Logout
 
Additional features :
1.   	FAQ – for better understanding
2.   	Feedback form – provided in the website
Check the below link for the working of our project :  https://drive.google.com/file/d/1LEkmx5sQx_3Z-UtwbxRXDg22sPduaoV-/view?usp=sharing
 
 
How to run the project:
We developed our project using Pycharm IDE , and follow the below instruction to setup the project
Prerequisites:
·         Python
·         Django Framework
 
Setup Django: ( run in terminal )
1.   	Pip install django
2.   	django-admin startproject project
3.   	django-admin startapp image
The django setup is done and the set of files provided by django will be visible , then replace those files with the code given in the repository , then run the below commands 
 
·         python manage.py makemigrations
·         python manage.py migrate
·         python manage.py createsuperuser 
After this command fill in the details – username , email , and setup a password ( accessible by admin ) for viewing your database
·         python manage.py runserver
This will generate a localhost link in the terminal open it to view DropBox website
 
 
If you want your project to be in public web address , follow the below instructions :
 
·         pip install pyngrok
·         In Settings.py file – ALLOWED_HOSTS = [‘localhost’ , ‘127.0.0.1’ , ‘.ngrok.io’]
·         Then , run your server – python manage.py runserver
·         Ngrok http 8000
·         This will generate a url for the website
 
 
 
 
 

