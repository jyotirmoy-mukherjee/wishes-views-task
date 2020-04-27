## Softwares
Python 3 and any preferred IDE
## Instructions
Work on the Birthday wishes API and reduce the code considerably using **APIViews** with    built-in HTTP method handlers.

The following are provided:

* A model `Wish`.
* Data added to the model to test the&nbsp;API.
* Appropriate URL conf.
* The serializer WishSerializer

Do the following:

1. In views.py:
    * Write the WishList class definition using ListCreateAPIView.
    * Write the WishDetail class definition using RetrieveUpdateDestroyAPIView.
2. In wishes/urls.py:
    * Modify the URLs to use the class-based views created. Part of the implementation is already provided.
	**Hint:** Use as_view().

To test the code, use the URL:
* /wishes/ to retrieve all the wishes.
* /wishes/ to post a new birthday wish.
* /wishes/{id}/ to retrieve a specific wish detail.
* /wishes/{id}/ to update an existing wish.
* /wishes/{id}/ to delete an existing wish.
## Commands
### Run
`python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py runserver 0.0.0.0:8000`
### Test
`python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py test`
### Install
`pip install -r requirements.txt`