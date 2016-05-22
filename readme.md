========================

This is the development repository for the Hello World Kind of Django Application


Development and HTTP Server
--------------------------------

This repository comes with a simple development and test server so that it is possible to develop
and test in an isolated environment. In order to use the test server, it is recommended that you
make a new dedicated Python virtual-environment:

```
virtualenv task_env (just do this once)

source task_env/bin/activate

pip install -r requirements.txt

./manage.py migrate

./manage.py runserver (run the test server)
```

API END POINT
-------------

You can view all the list of the users info by hitting the url

```
$BASEURL/api/v1/userinfo
```
This API endpoint is protected by token authentication. You can get authentication
token from django admin panel.
