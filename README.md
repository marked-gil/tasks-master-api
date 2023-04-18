# Tasks Master API
This is the API for that serves the **Tasks Master** React application. This API is developed using the [Django Rest Framework](https://www.django-rest-framework.org/) and contains 4 models: profiles, categories, tasks, and comments. Click [Here](http://tasks-master.herokuapp.com/) for the live **Tasks Master** React application.

**Tasks Master**
[View Live Website.]

## TABLE OF CONTENTS


## **Development Goal:**

## **The Use of Agile Methodology**

[<ins>Back to Table of Contents</ins>](#table-of-contents)

### **EPICS:**
1. [Initial Project Setup](https://github.com/marked-gil/tasks-master-api/issues/1)
2. [Data Models](https://github.com/marked-gil/tasks-master-api/issues/2)
3. [Model Serializers](https://github.com/marked-gil/tasks-master-api/issues/3)
4. [Profiles](https://github.com/marked-gil/tasks-master-api/issues/4)
5. [Tasks](https://github.com/marked-gil/tasks-master-api/issues/5)
6. [Categories](https://github.com/marked-gil/tasks-master-api/issues/7)
7. [Comments](https://github.com/marked-gil/tasks-master-api/issues/8)
8. [Authentication and Authorization](https://github.com/marked-gil/tasks-master-api/issues/10)
9. [API Deployment](https://github.com/marked-gil/tasks-master-api/issues/11)

[<ins>Back to Table of Contents</ins>](#table-of-contents)


### **User Stories**

The following are the User Stories that guided the creation of this API:
* **User Story:** [**Setup Django and Cloudinary for API**](https://github.com/marked-gil/tasks-master-api/issue)
    > As a developer, I want Django and Cloudinary installed, so that I can create the initial Django app and connect it to Cloudinary as storage.

    Implementation:      
    * Install Django, django-cloudinary-storage, and Pillows libraries
    * Configure settings.py to include the Cloudinary storage by importing it as an environment variable.
    * Add ‘cloudinary_storage’ and ‘cloudinary’ in setting.py’s INSTALLED_APPS

* **User Story:** [**Initial Setup of the API's Environment**](https://github.com/marked-gil/tasks-master-api/issues/13)    
    > As a developer, I want to create environment variables so sensitive information or data can be protected.

    Implementation:
    * Create an env.py in the top directory
    * Place all sensitive data inside the env.py file, e.g. ‘cloudinary URL’, ‘Django Secret Key’
* **User Story:** [**Profile Model**](https://github.com/marked-gil/tasks-master-api/issues/14) 
    > As a developer, I can automatically create a profile for each signed-up user so that they can add other personal information such as name, email, and profile picture.

    Implementation: 
    * Create the ‘profiles’ app
    * Add the ‘profiles’ app in setting.py’s INSTALLED_APPS
    * Create a Profile model with fields, such as id, owner, first_name, last_name, image, email, datetime_created, datetime_updated, etc.
    *Register the Profile model in the admin.py
* **User Story:** [**Task Model**](https://github.com/marked-gil/tasks-master-api/issues/15)
    > As a developer, I can save in the database the tasks created by users so they can be returned on request.     

    Implementation: 
    * Create ‘tasks’ app
    * Add the ‘tasks’ app in setting.py’s INSTALLED_APPS
    * Create a Task Model with fields, such as id, owner, task_name, details, datetime_created, datetime_updated, due_date, due_time, category, priority, progress, etc.
    * Register the Task Model in the admin.py
* **User Story:** [**Category Model**](https://github.com/marked-gil/tasks-master-api/issues/17)
    > As a developer, I can save categories to the database so tasks are categorized.       

    Implementation: 
    * Create ‘categories’ app
    * Add the ‘categories’ app in settings.py’s INTALLED_APPS
    * Create a Category model with fields, such as owner, category_name, description, datetime_created, datetime_updated, etc.
    * Register the Category model in the admin.py
* **User Story:** [**Comment Model**](https://github.com/marked-gil/tasks-master-api/issues/18)
    > As a developer, I can allow users to create comments on tasks and save them in the database.

    Implementation: 
    * Create ‘comments’ app
    * Add the ‘comments’ app in settings.py’s INSTALLED_APPS
    * Create a Comment model with fields, such as id, owner, content, datetime_created, datetime_updated, task, reply_to, is_reply_to_comment, etc.
    * Register the Comment model in the admin.py
* **User Story:** [**Setup Django REST Framework**](https://github.com/marked-gil/tasks-master-api/issues/20)   
    > As a developer, I can use the Django REST Framework to build the API so it will be quick, reliable, and secure.

    Implementation:
    * Install Django REST Framework - djangorestframework
    * Add the ‘rest_framework’ in settings.py’s INSTALLED_APPS
* **User Story:** 
    Implementation:
* **User Story:** 
    Implementation:
* **User Story:** 
    Implementation:
* **User Story:** 
    Implementation:
* **User Story:** 
    Implementation:
* **User Story:** 
    Implementation:


[<ins>Back to Table of Contents</ins>](#table-of-contents)

## **API Endpoints**

## **Database Schema**

## Features

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## Features Left for Future Implementation

## Fixed Bugs

* ISSUE: I was migrating my app models to the production database but I got an error: `django.db.utils.ProgrammingError: cannot cast type integer to uuid` in my **comments** app. And so, I thought the easiest way to do was to delete my migration files from the `migrations` directory (which, now I learned, is not the best way to solve it). Unfortunately, when I did the migration again, I was presented with another error: `django.db.migrations.exceptions.InconsistenMigrationHistory`.

    * INTENDED OUTCOME:     
    I want my models to be succesfully migrated to my PostgreSQL database to allow my application to run smoothly in production.

    * SOLUTION:     
    As I do not have much data stored in the database yet, I just deleted the old database and created a new one. After having done that, I did the migration again. This time it worked. I got the idea to solve it from this link: https://forum.djangoproject.com/t/django-db-migrations-exceptions-inconsistenmigrationhistory/14129

## Bugs Left To Fix

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## Testing

## Deployment

### **Version Control**

**Git** was a crucial tool used to track changes that were made in the repository. The following git commands were mainly used in developing this program:

* `git status` — to show the status of the repository by displaying the files that have been staged and are ready for commit, those that are not, and those that are untracked. 
* `git add <file name>` — to add file or changes in the file to the staging area before they can be committed
* `git commit -m "message"` — to add/record files or changes to the local repository
* `git push` — to upload the local repository to the remote repository, such as GitHub

### **Heroku Deployment**


### **Cloning from GitHub**

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## Technologies
This project uses the following tools:
* Backend Programming Language:
    * [Python](https://www.python.org/)
* Web Framework:
    * [Django](https://www.djangoproject.com) - web framework used in developing this project
    * [Django REST Framework](https://www.django-rest-framework.org/) - toolkit used to build this web API
* Deployment Platform:
    * [Heroku](https://www.heroku.com) - the cloud platform used for deployment of the website
* Media and Asset Storage:
    * [Cloudinary](https://cloudinary.com/) - where the assets of this project, including photos are stored
* Database:
    * [ElephantSQL](https://www.elephantsql.com/) - serves as the PostgreSQL database for this project
* Modules and Libraries:
    * [django-database-url](https://pypi.org/project/dj-database-url/) - used for connecting Django to database
    * [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - facilitates integration with Cloudinary by implementing Django Storage API
    * [cloudinary](https://pypi.org/project/cloudinary/) - to quickly and easily integrate the application with Cloudinary
    * [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/index.html) - a set of REST API endpoints to handle User Registration and Authentication tasks.
    * [Simple JWT]((https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)) (`djangorestframework-simplejwt`) - provides a JSON Web Token authentication backend for the Django REST Framework
    * [datetime module](https://docs.python.org/3/library/datetime.html) - used for the created dates in the project
    * `OS` module in Python - used in the `settings.py` file to perform functions that involve the operating system, such as checking for environment variables

* [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/) - as Django secret_key generator
* `Git` - as a version control system, was used to monitor and record changes made when building the site. This allowed for the restoration of an earlier version of the code when it was necessary
* `Gitpod` - the cloud-based IDE (Integrated Developer Environment) used to code this site
* `GitHub` - stores the source code repository for this website
* [Diffchecker](https://www.diffchecker.com/#) - used when comparing codes tested in another IDE to the codes in gitpod     
* [Grammarly](https://www.grammarly.com/) - used to check the grammar of the contents in this project   
* Web browsers (Google Chrome, Firefox, Safari, Microsoft Edge) 
* For Testing and Validation:   
    * [CI Python Linter](https://pep8ci.herokuapp.com/) 

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## Credits

* [Stackoverflow](https://stackoverflow.com/questions/65908861/how-to-automatically-create-new-profile-once-a-new-user-is-created-in-django) - How to automatically create a profile for registered users using @receiver decorator and Django signal
* [Stackoverflow](https://stackoverflow.com/questions/29642390/how-to-filter-serializers-slugrelatedfield-queryset-using-model-field) - Modifying SlugRelatedField to return a filtered queryset
* [Code Institute's drf-api repo](https://github.com/Code-Institute-Solutions/drf-api/blob/c637122d1a559139cabf1d39b0a3281814091d79/posts/serializers.py) - Code for the image validation
* [Edureka! Community](https://www.edureka.co/community/74191/how-update-date-automatically-after-value-change-in-django) - How to update a date automatically when a value changes in Django


### References
* Main References:
    * [Code Institute](https://codeinstitute.net/ie/)
    * [Django Documentation](https://docs.djangoproject.com/en/3.2/)    

## Acknowledgment