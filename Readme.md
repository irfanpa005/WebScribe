## Distinctiveness and Complexity

WebScribe offers a comprehensive set of features to users, encompassing three core functions,with the added benefit of JavaScript for a seamless and responsive user experience.

#### 1. Note Creation

Note creation feature empowers users to document their thoughts, ideas, and important information with ease. Unlike many standalone note-taking applications, using a library called ck-editor helps user to create notes in a RichTextField which provides many text formatting facilities and media attaching and more features. User even have the option to share notes with the public, making knowledge sharing a breeze.

#### 2. Todo Task Manager

The todo task manager provides a dynamic and flexible approach to task management. Users can organize their tasks, set priorities, and track progress efficiently. Distinct from other task managers, task cards show the remaining days to complete task. Also tasks can be viewed on prioritized or grouped way.

#### 3. Tutorials Section

The reference section serves as a repository for tutorials, links, and other resources. User can share curated list of links with others, fostering a learning community. Never lose track of valuable resources again with our link-saving feature.

### Collaborative Capabilities

One of the most complex and unique aspects of our project is its collaborative nature. Users can share their notes, tasks, and references with other users, fostering teamwork and knowledge exchange. Collaborative features include:


- **User Authentication:** We've implemented secure user authentication to protect user data and privacy. Sigin for users i smade       simple by allowing users to sign in with their Google accounts.



## Project Structure
notes app - Handles notes and tutorials functions of registered or signed in users.
toDo app - Handles todo tasks of registered or signed in users.
userApp - Handles usercreation, authentication, shared datas to the non-registered users.

## Python packages used
packages requirements are mentioned in 'requirements.txt' file.

django framework

ck-editor - RichTextfield editor used for notes creation and editing.Settings are done in project settings.py. for any further updation or changes you can refer.
https://pypi.org/project/django-ckeditor/

django-crispy-forms,crispy-bootstrap5
makes to manage the django forms
https://pypi.org/project/django-crispy-forms/

django-allauth
used for sign in using google or social media account. In addition to configuring in project, we will need to configure web application in google developer console for authentication and in social applications in django admin panel. please do refer.
https://pypi.org/project/django-allauth/
https://learndjango.com/tutorials/django-allauth-tutorial

## Project hosted link
http://webscribe.pythonanywhere.com/
