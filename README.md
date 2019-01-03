# Problem Statement
A company has 10 versions of an image they intend using to run an advert to the users of their website and the projection of the cost 
of doing A | B testing is quite high so they need to find a to explore these ads while at the same time exploiting the one with the most
user click (i.e they need a program that displays the ads to users and at the same time is calculating which one is having the most impact
thereby converging the particular ad being shown to the ones with highest user clicks).

# Full breakdown
I gave a full tutorial on what's really happening with this project in this 
[Medium Post](https://medium.com/@wilpat456/thompson-sampling-with-django-ce13548dc2a4)

# Installation
Clone the repo

Create your django environment where you install django ( Here's a great [tutorial](https://poweruphosting.com/blog/install-django) on how
to do this on different operating systems)

Navigate into the project

run `python manage.py makemigrations`

run `python manage.py migrate`

If you want to be access the admin section of this project do this: 

run `python manage.py createsuperuser` (You'd be prompted to choose a username and a password)

Finally run `python manage.py runserver` and you're good to go.
