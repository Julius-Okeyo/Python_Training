## .venv files
The .venv directory was created with our virtual environment but Django
has added a Hello_World directory and a manage.py file. Within
django_project are five new files:
### __init__.py
Indicates that the files in the folder are part of a Python
package. Without this file, we cannot import files from another
directory which we will be doing a lot of in Django!
### asgi.py
Allows for an optional Asynchronous Server Gateway
Interface to be run
### settings.py
Controls our Django project’s overall settings
### urls.py
Tells Django which pages to build in response to a browser or
URL request
### wsgi.py
Stands for Web Server Gateway Interface which helps Django
serve our eventual web pages.
### manage.py
Is not part of django_project but is used to execute
various Django commands such as running the local web server or creating
a new app.
## Model-View-Controller vs Model-View-Template
Over time the Model-View-Controller (MVC) pattern has emerged as a
popular way to internally separate the data, logic, and display of an
application into separate components. This makes it easier for a developer
to reason about the code. The MVC pattern is widely used among web
frameworks including Ruby on Rails, Spring (Java), Laravel (PHP),
ASP.NET (C#) and many others.
In the traditional MVC pattern there are three major components:
Model: Manages data and core business logic
View: Renders data from the model in a particular format
Controller: Accepts user input and performs application-specific logic
Django only loosely follows the traditional MVC approach with its own
version often called Model-View-Template (MVT). This can be initially
confusing to developers with previous web framework experience. In
reality, Django’s approach is really it is a 4-part pattern that also
incorporates URL Configuration so something like MVTU would be a more
accurate description.
The Django MVT pattern is as follows:
Model: Manages data and core business logic
View: Describes which data is sent to the user but not its presentation
Template: Presents the data as HTML with optional CSS, JavaScript,
and Static Assets
URL Configuration: Regular-expression components configured to a
View
This interaction is fundamental to Django yet very confusing to newcomers
so let’s map out the order of a given HTTP request/response cycle. When
you type in a URL, such as https://djangoproject.com, the first thing
that happens within our Django project is a URL pattern (contained in
urls.py) is found that matches it. The URL pattern is linked to a single
view (contained in views.py) which combines the data from the model
(stored in models.py) and the styling from a template (any file ending in
.html). The view then returns a HTTP response to the user.
The complete Django flow looks like this:
Django request/response cycle
HTTP Request -> URL -> View -> Model and Template -> HTTP Response
If you are brand new to web development the distinction between MVC and
MVT will not matter much. This book demonstrates the Django way of
doing things so there won’t be confusion. However if you are a web
developer with previous MVC experience, it can take a little while to shift
your thinking to the “Django way” of doing things which is more loosely
coupled and allows for easier modifications.
## Create An App
Django uses the concept of projects and apps to keep code clean and
readable. A single top-level Django project can contain multiple apps. Each
app controls an isolated piece of functionality. For example, an e-commerce
site might have one app for user authentication, another app for payments,
and a third app to power item listing details. That’s three distinct apps that
all live within one top-level project. How and when you split functionality
into apps is somewhat subjective, but in general, each app should have a
clear function.
To add a new app go to the command line and quit the running server with
Control+c. Then use the startapp command followed by the name of our
app which will be pages.
Shell
##### Windows
(.venv) > python manage.py startapp pages
##### macOS
(.venv) % python3 manage.py startapp pages
If you look visually at the helloworld directory Django has created within
it a new pages directory containing the following files:
Code
├── pages
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations
│ │ └── __init__.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
Let’s review what each new pages app file does:
### admin.py
Is a configuration file for the built-in Django Admin app
### apps.py
Is a configuration file for the app itself
migrations/ keeps track of any changes to our models.py file so it
stays in sync with our database
### models.py
Is where we define our database models which Django
automatically translates into database tables
### tests.py
Is for app-specific tests
### views.py
Is where we handle the request/response logic for our web
app
Notice that the model, view, and url from the MVT pattern are present from
the beginning. The only thing missing is a template which we’ll add shortly.
Even though our new app exists within the Django project, Django doesn’t
“know” about it until we explicitly add it to the
django_project/settings.py file. In your text editor open the file up and
scroll down to INSTALLED_APPS where you’ll see six built-in Django apps
already there. Add pages.apps.PagesConfig at the bottom.
Code
### django_project/settings.py
INSTALLED_APPS = [
 "django.contrib.admin",
 "django.contrib.auth",
 "django.contrib.contenttypes",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.staticfiles",
 "pages.apps.PagesConfig", # new
]
If you have Black installed in your text editor on “save” it will change all
the single quotes '' here to double quotes "". That’s fine. As noted
previously, Django has plans to adopt Black Python formatting fully in the
future.
What is PagesConfig you might ask? Well, it is the name of the solitary
function within the pages/apps.py file at this point.
Code
### pages/apps.py
from django.apps import AppConfig
class PagesConfig(AppConfig):
 default_auto_field = "django.db.models.BigAutoField"
 name = "pages"
