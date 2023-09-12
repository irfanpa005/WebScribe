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
Webscribe is a versatile web application designed to cater to the diverse needs of continuous learners, students, and task managers. This application serves as your digital workspace, providing a unified solution for note-taking, tutorial link saving, and task management.  Enjoy the convenience of rich text editing, allowing you to format your notes with headers, lists, images, and more. Users can also share the notes and tutorials with other users if they wish making knowledge sharing a breeze.

My Motivation for this project was conceived from a passion for continuous learning and a recognition of the challenges faced by learners who need to take notes, save tutorials, and manage tasks effectively. I understand that all continuous learners benefit from a digital workspace to organize their knowledge and tasks efficiently. The desire to facilitate easy note-taking, tutorial saving, along with the ability to share these resources, inspired me to create this project. I believe that Webscribe provides a valuable tool for learners and knowledge enthusiasts seeking a comprehensive and user-friendly solution for their needs.

## Distinctiveness and Complexity

I believe that Webscribe is distinctive from other projects because, unlike other projects, Webscribe is a multifunctional platform that combines note-taking, tutorial saving, and task management within a single integrated platform, catering to continuous learners and information enthusiasts. Unlike social websites, where content is often public by default, the Webscribe platform empowers users to make their content private or public, providing robust privacy controls. In addition to Django authentication, social authentication, or Google authentication functionality is used to make user sign-in easy.

I believe that the project is complex because multiple Django apps and models are used for the Project. The intricacy arises from the interrelation between these models, particularly with the user model where userApp model fields are used in other models to link data with users. Furthermore, the project incorporates JavaScript in the front-end and back-end to fetch data from the database. This dual-purpose use of JavaScript adds another layer of complexity, enabling dynamic data retrieval and manipulation, enhancing the user interface, and ensuring a responsive application.

The website is designed with a responsive design feature that ensures seamless functionality and optimal user experience across various devices and screen sizes.


## File structure description
Overview of file structure.
```plaintext
.Webscribe/(root folder)
│
├───notes - notes app used for the functionality of notes and tutorials making of registered users.  
│   ├───...                                
│   ├───models.py - contains models for notes and tutorials.
│   ├───forms.py - django forms for notes and tutorials.
│   ├───views.py - views functionality for notes and tutorials.
│   │───urls.py - defines the notes application's URL patterns and routes.
│   │───...     
│   └───
│
├───ProjectScribe -- django project folder.
│   ├───...    
│   ├───static  -- static folder for the project.
│   │   ├───css
│   │   ├───images -- contains images, logo, and favicons of the project. 
│   │   └───js -- contains all javascript files.
│   ├───settings.py -- general settings of the project including ck-editor settings and social auth app setting. 
│   └───....
│
├───static
│   └─── This static folder contains files required for the ck-editor library. The project static folder is created inside the 'ProjectScribe' directory to avoid confusion. You don't need to do any changes inside.
│   
│
├───templates -- contains all HTML templates used for the project.
│   
├───toDo -- toDo app folder. contains files for ToDo task functionality.
│   ├───...                                
│   ├───models.py - contains models for todo task.
│   ├───forms.py - django forms for for todo task.
│   ├───views.py - views functionality for todo task.
│   │───urls.py - defines the toDo application's URL patterns and routes.
│   └───...
│
├───userApp - userApp app folder. userApp handles the user registration, Google auth functionality, and page visibility functions for non-signed users.  
│   ├───...                                
│   ├───models.py - contains models for user registration.
│   ├───forms.py - django forms for user registration.
│   ├───views.py - views functionality for user creation and page visibility for non-signed users.
│   ├───urls.py - the URLs related to userApp and URL to redirect user for Google sign in.     
│   └───...
```

## How to run
1. Clone the git repository.
2. Make sure Python is installed(version 3.11.1)
3. Make a Virtual environment for the project.
4. Install the Django framework (Django version used is 3.2).
5. Install all Packages added in 'requirements.txt'.
6. Create a superuser to manage the database and access the admin panel.
```bash
python manage.py createsuperuser
``` 
7. Do make migrations from console
```bash
python manage.py makemigrations
```
8. Do migrate from console
```bash
python manage.py migrate
```
9. Run server
```bash
python manage.py runserver
```

## Additional Information
 Python packages that need to be installed in order to run the web application, are mentioned in the requirements.txt file!

 The project offers the convenience of Google authentication for user sign-in, making it easy for users to access their accounts. However, it's  optional and not a mandatory requirement for running the application. If you prefer not to use it, you have the flexibility to remove the Google sign-in button from the index.html HTML template. If you decide to enable Google authentication for the Project instance, follow the steps in the below URL to set it up.<br>
https://www.codesnail.com/google-authentication-in-django/


## Project demonstration video<br>
https://youtu.be/TFmnt0KTfVE


## Project hosted link
http://webscribe.pythonanywhere.com/<br>


## Acknowledgements
I would like to express my sincere gratitude to CS50, David J. Malan, and Brian Yu for their excellent guidance and for making complex concepts easy to understand through CS50 Web Programming with Python and Javascript.
