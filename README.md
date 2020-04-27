## Softwares
Python 3 and any preferred IDE
## Given
Work on the Birthday wishes API and reduce the code considerably using **APIViews** with    built-in HTTP method handlers.

The following are provided:

* A model `Wish`.
* Data added to the model to test the API.
* Appropriate URL conf.
* The serializer `WishSerializer`
* The `permissions.py` file with `IsOwnerOrReadOnly` permission definition
* `UserList` and `UserDetail` to view users who can login and post wishes
* Two users __agbeadmin__ and __agbeuser__ both with password __frescopassword__

## Instructions
Do the following:
### Enable Views
1. In `views.py`:
    * Write the `WishList` class definition using `ListCreateAPIView`.
    * Write the `WishDetail` class definition using `RetrieveUpdateDestroyAPIView`.
2. In `wishes/urls.py`:
    * Modify the URLs to use the class-based views created. Part of the implementation is already provided.
	**Hint:** Use as_view().
### Enable Security
1. Add the owner field in `Wish` model referring to `User`
2. Add a owner field definition in `WishSerializer`
3. In `views.py`:
    * In the `WishList` class definition:
        * Add permissions for authenticated users to post wishes (anyone can view wishes)
        * Associate wishes a logged-in user by modifying the perform_create method
    * In the `WishDetail` class definition:
        * Add permission for authenticated users to update and delete a wish
        * Add permissions so that only the owner can update or delete (others can only view). **Hint:** Use the class definition from the `permissions.py` file
4. In `serializers.py`:
    * Create `UserSerializer` class definition
    * Add a 'wishes' column as a `PrimaryKeyRelatedField`, and add it to the fields
5. In `exercise3/urls.py` file:
    * Add a url pattern to include the login and logout views for the browsable API

To test the code, use the URL:
* /wishes/ to retrieve all the wishes.
* /wishes/ to post a new birthday wish.
* /wishes/{id}/ to retrieve a specific wish detail.
* /wishes/{id}/ to update an existing wish.
* /wishes/{id}/ to delete an existing wish.
* Login as agbeadmin user, and try the above URLs. Then, login as agbeuser, and try the above URLs
* Observe the API behavior


## Commands
### Run
`python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py runserver 0.0.0.0:8000`
### Test
`python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py test`
### Install
`pip install -r requirements.txt`