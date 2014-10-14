# db_stud

Создать django проект который управляет базой студентов, Сущности:
Студент - ФИО, дата-рождения, №студ-билета, группа(FK(Группа))
Группа - Название, староста(FK(Студент))
Проект должен быть сконфигурирован на sqlite и иметь фикстуру
initial_data.json с подготовленными данными(несколько групп и студентов)
 Создать следующие views:
      - список групп (таблица - название, кол-во человек в группе,
староста)
      - при нажатии на группу - страница с со списком студентов для
этой группы
      - создание/редактирование/удаление  групп/студентов
Добавить авторизацию для этих страниц (username/password)
Добавить авторизацию email+password

и еще:

Сделать middleware который на всех страницах(content-type ==
text/html) добавляет время выполнения запроса и количество sql
запросов(перед закрывающим тегом </body>)
Django.Admin - создать admin views для Групп/студентов (студенты
так же должны быть как inline для Групп)
Шаблоны/Контекст - сделать template-context-processor который
добавляет django.settings в контекст шаблонов
Шаблоны/Теги - написать тег который принимает любой объект и
рендерит ссылку на его редактирование в админке (например {% edit_list
request.user %})
Сигналы - написать обработчики сигналов которые для каждой модели
создает запись в базе о ее  создании/редактировании/удалении
Команды - написать django команду которая выводит список групп и
студентов в группе в консоль (что такое django-команда -
http://webnewage.org/2008/02/05/komandovat-paradom-budet-django/)
Django.TestFramework - написать django-testcase (unittest) который
логинится на сайт, добавляет группу и студента

на фронтенде angular.js
на бекенде данные отдаются через rest json api с использованием django-rest-framework


This is student database written with django and angularjs.
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
