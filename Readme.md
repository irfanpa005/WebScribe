# Webscribe <span style="font-size:medium;">(cs50Web Final Project)</span>

## Table of Contents
<ul>
  <li>Project Overview</li>
  <li>Distinctiveness and Complexity</li>
  <li>Contributed Files</li>
  <li>Installation</li>
  <li>How to Run</li>
  <li>Python Packages</li>
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
│   └───...
│
├───userApp - userApp app folder. userApp handles the user registration, google auth functionality, and page visibility functions for non-signed users.  
│   ├───...                                
│   ├───models.py - contains models for user registration.
│   ├───forms.py - django forms for user registration.
│   ├───views.py - views functionality for user creation and page visibility for non-signed users.
│   ├───urls.py - the urls related to userApp and url to redirect user for google sign in.     
│   └───...


#### 1. Note Creation

Note creation feature empowers users to document their thoughts, ideas, and important information with ease. Unlike many standalone note-taking applications, using a library called ck-editor helps user to create notes in a RichTextField which provides many text formatting facilities and media attaching and more features. User even have the option to share notes with the public, making knowledge sharing a breeze.

#### 2. Todo Task Manager

The todo task manager provides a dynamic and flexible approach to task management. Users can organize their tasks, set priorities, and track progress efficiently. Distinct from other task managers, task cards show the remaining days to complete task. Also tasks can be viewed on prioritized or grouped way.

#### 3. Tutorials Section

The reference section serves as a repository for tutorials, links, and other resources. User can share curated list of links with others, fostering a learning community. Never lose track of valuable resources again with our link-saving feature.

### Collaborative Capabilities

One of the most complex and unique aspects of our project is its collaborative nature. Users can share their notes, tasks, and references with other users, fostering teamwork and knowledge exchange. Collaborative features include:


**User Authentication:** We've implemented secure user authentication to protect user data and privacy. Sigin for users i smade       simple by allowing users to sign in with their Google accounts.


## Project Structure
notes app - Handles notes and tutorials functions of registered or signed in users.<br>
toDo app - Handles todo tasks of registered or signed in users.<br>
userApp - Handles usercreation, authentication, shared datas to the non-registered users.

## Python packages used
packages requirements are mentioned in 'requirements.txt' file.<br>

django framework<br>

ck-editor - RichTextfield editor used for notes creation and editing.Settings are done in project settings.py. for any further updation or changes you can refer.<br>
https://pypi.org/project/django-ckeditor/<br>

django-crispy-forms,crispy-bootstrap5<br>
makes to manage the django forms<br>
https://pypi.org/project/django-crispy-forms/<br>

django-allauth<br>
used for sign in using google or social media account. In addition to configuring in project, we will need to configure web application in google developer console for authentication and in social applications in django admin panel. please do refer.<br>
https://pypi.org/project/django-allauth/<br>
https://learndjango.com/tutorials/django-allauth-tutorial<br>

## Project hosted link
http://webscribe.pythonanywhere.com/<br>
