# Webscribe <span style="font-size:medium;">(cs50Web Final Project)</span>

## Table of Contents
<ul>
  <li>Project Overview</li>
  <li>Distinctiveness and Complexity</li>
  <li>File structure</li>
  <li>How to Run</li>
  <li>Additional Information</li>
  <li>Project demonstration video</li>
  <li>Project hosted link</li>
  <li>Acknowledgements</li>
</ul>

## Project Overview
Webscribe is a versatile and feature-rich web application designed to cater to the diverse needs of continuous learners, information enthusiasts, and task managers. This application serves as your digital workspace, providing a unified solution for note-taking, tutorial and link saving, and task management.  Enjoy the convenience of rich text editing, allowing you to format your notes with headers, lists, images, and more. Users can also share the notes and tutorials with other users if they wish making knowledge sharing a breeze.

## Distinctiveness and Complexity

I believe that Webscribe is distinctive from other projects because, unlike other projects, Webscribe is a multifunctional platform that combines note-taking, tutorial saving, and task management within a single integrated platform, catering to continuous learners and information enthusiasts.Different from social websites, where content is often public by default, the Webscribe platform empowers users with the choice to make their content private or public, providing robust privacy controls. In addition to Django authentication, social authentication, or Google authentication functionality is used to make user sign-in easy.

I beleive that project is complex in the sense that multiple Django apps and models are used for Project. The intricacy arises from the interrelation between these models, particularly with the user model where userApp model fields are used in other models to link datas with users. Furthermore, project incorporates JavaScript not only in the front-end but also in the back-end to fetch data from the database. This dual-purpose use of JavaScript adds another layer of complexity, enabling dynamic data retrieval and manipulation, enhancing the user interface, and ensuring a responsive application.

Website is designed with responsive design feature that ensures seamless functionality and optimal user experience across various devices and screen sizes.


## File structure description
Overview of file strucuture.
```plaintext
.Webscribe/(root folder)
│
├───notes - notes app used for functionality of notes and tutorials making of registered users.  
│   ├───...                                
│   ├───models.py - contains models for notes and tutorials.
│   ├───forms.py - django forms for notes and tutorials.
│   ├───views.py - views functionality for notes and tutorials.
│   │───urls.py - defines the notes applcation's URL patterns and routes.
│   │───...     
│   └───
│
├───ProjectScribe -- django project folder.
│   ├───...    
│   ├───static  -- static folder for project.
│   │   ├───css
│   │   ├───images -- contains images,logo and favicons of project. 
│   │   └───js -- contains all javascript files.
│   ├───settings.py -- general settings of project including ck-editor settings and social auth app setting. 
│   └───....
│
├───static
│   └─── this static folder contains files required for ck-editor library. Project static folder is created inside 'ProjectScribe' directory to avoid confusion. you dont need to do any chnages inside.
│   
│
├───templates -- contains all HTML templates used for project.
│   
├───toDo -- toDo app folder. contains files for ToDo task functionality.
│   ├───...                                
│   ├───models.py - contains models for todo task.
│   ├───forms.py - django forms for for todo task.
│   ├───views.py - views functionality for todo task.
│   │───urls.py - defines the toDo applcation's URL patterns and routes.
│   └───...
│
├───userApp - userApp app folder. userApp handles the user registration, google auth functionality, and page visibility functions for non-signed users.  
│   ├───...                                
│   ├───models.py - contains models for user registration.
│   ├───forms.py - django forms for user registration.
│   ├───views.py - views functionality for user creation and page visibility for non-signed users.
│   ├───urls.py - the urls related to userApp and url to redirect user for google sign in.     
│   └───...
```

## How to run
1. Clone the git repository.
2. Make sure Python is installed(version 3.11.1)
2. Make Virtual environment for the project.
2. Install Django framework, Modules and Packages.Django version used is 3.2.
```bash
pip install requirements.txt
```
3. Do make migrations from console
```bash
python manage.py makemigrations
```
4. Do migrate from console
```bash
python manage.py migrate
```
5. Run server
```bash
python manage.py runserver
```
6. Create a superuser to manage database and access admin panel.
```bash
python manage.py createsuperuser
```

## Additional Information
 Python packages that need to be installed in order to run the web application, is mentioned in requirements.txt file!.

 Project offers the convenience of Google authentication for user sign-in, making it easy for users to access their accounts. However, it's  optional and not a mandatory requirement for running the application. If you prefer not to use it, you have the flexibility to remove the Google sign-in button from the index.html HTML template. If you decide to enable Google authentication for Project instance, follow the steps in below url to set it up.<br>
https://www.codesnail.com/google-authentication-in-django/


## Project demonstration video<br>
https://youtu.be/kvjaIvK3EMQ


## Project hosted link
http://webscribe.pythonanywhere.com/<br>


## Acknowledgements
I would like to express my sincere gratitude to cs50, David J. Malan and Brian Yu for their excellent guidance and making complex concepts easy to understand through cs50 Web Programming with Python and Javascript.
