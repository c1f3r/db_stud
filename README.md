# db_stud
This is student database written with django and angularjs.

You can see demo [here](http://cifer-dbstud.herokuapp.com/)

Login/password: admin/admin

Also you can use email admin@example.com as login.

Test project made by tasks in [test.txt](https://github.com/c1f3r/db_stud/blob/master/test.txt)

To install it you should follow next steps:
First of all you need to create `virtualenv` for you project:

`virtualenv db_stud`

Then you should activate it:

`cd db_stud`

`source bin/activate`

Clone from git:

`git clone https://github.com/c1f3r/db_stud`

`cd db_stud`

Install requirements:

`pip install -r requirements.txt`

Initialize database:

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py loaddata initial_data/initial_data.json`


There is a command for displaying groups list:

`python manage.py list_all`
