# Project 4
- This is my project 4 submission for Code Institute where I have created a Pokemon blog where you can look at topics of Pokemon and create a blog and interact with others using comments. I have created to display my skills in using autentication and CRUD skills. 
I have always been passionate about Pokemon so I wanted to create a simple pokemon blog style application that is easy and friendly to use and just have some fun when creating a blog post :).
- Here is a link to the Heroku deployed website https://blog-pokemon-24f5118ca311.herokuapp.com/
- Here is a link to my github https://github.com/aokealy/blog-pokemon
# User Experience (UX):

## Mock Up:
- Mockup design on all platforms such as Desktop, Laptop, Tablet and Mobile Phone.
- Easy and clear view of all links and nice spacing for each platform.
- Mobile Friendly and tablet friendly.
- ![Screenshot](/media/mockup-image.png)

## Wireframes:
- Login and Register wireframe
- Start always on the Login Page when accessing the website.
- Easy to find on Front Page in Navbar and simple proccess to to either register or login. Most commonly found on the right side of the navigation bar in a lot of different websites so it gives familiarity.
- ![Screenshot](/media/wireframe-login.PNG)

- Core page wireframe
- Split the core page into two sections where everything is displayed such as the create blog and displaying the blogs. My idea is that everything is on one page and not split into different pages which could confuse the user so I decided it would be best to display into two sections instead. 
- ![Screenshot](/media/wireframe-core.PNG)

- accounts page wireframe
- Friendly Icons and good colours when looking at editing your account and looking at the account which gives you a friendly vibe and easily layed out to change name and email.
- ![Screenshot](/media/wireframe-account.PNG)

- Blog Detail wirframe
- View the blog where I the text is centered and easily readable alongside adding a comment section underneath where you can view if anyone has made a comment or not and also have CRUD function buttons for your own personal blog post.
- ![Screenshot](/media/wireframe-blog-detail.PNG)

## Agile User Stories:
- Here is a link to my user stories: 
- I followed this guidline and mapped three cards using Kanban board to determine what was next such as todo, progress and done for completion of my user stories and made sure to follow through and complete each task as I went along during this project. 

- https://github.com/aokealy/blog-pokemon/projects?query=is%3Aopen

## Document User Stories:
### User Story Login: (Completed)
- User can access login page from when they access website
- User be able to Login after the have registered
- User to be redirected after logging in

### User Story Registration: (Completed)
- User to be able to register without going to admin.
- User to be able to easily signup with clear and easy layout for user
- User to be able to access the register page from main menu
- User can create username when registering
- User can log in after creating an account

### User Story Logout: (Completed)
- User can logout of blog and would be redirected back to login page.
- User will no longer have access to main page until user logs back in.

### User Story Access Core Page: (Completed)
- User is able to view the core page when the user finishes logging in.
- User will see Blog Posts and can create blog posts.
- User will have navbar on main page with features such as account and logout.

### User Story Create Blog: (Completed)
- User be able to create a blog post with a title and description
- User can see there blog post created
- User can create many blogs.
- User will only be able to see this blog when logged in.

### User Story View Blog Page: (Completed)
- User can click on any blog that is displayed
- User click on any title of blog to access blog page
- User can scroll down to see all blog posts
- User can leave a comment on blog post
- User can edit or delete own blog post
- User cannot delete other user's blog posts.

### User Story Edit Blog Post: (Completed)
- User who created a blog when clicking on that blog will see an edit button where the user can edit and change the title and description of that blog page.
- User will be able to confirm change and will update after updating it.

### User Story Delete Blog Page: (Completed)
- User can delete a blog page that they created by clicking on the delete button that will bring them to the delete page and give them a choice of deleting the blog or cancel deleting the blog.
- User after cancelling the delete blog will be redirected back to the blog post itself.
- User who delete blog post will be redirected back to main page.

### User Story Access Account Page: (Completed)
- User can access account page and view there account details on that page.
- User will have edit button on account page
- User can see account Username and Email on account page.

### User Story Edit Account Page: (Completed)
- User can edit their account page such as username and email.
- User can go back or choose to confirm profile changes.
- Both buttons will redirect user back to account page.

### User Story Leave Comment: (Completed)
- User can click on any blog post and leave a comment under the blog post.
- User blog post comment count will increase based on how many comments are on that blog post.
- User can access the comments and see who wrote a comment on that post.







# Design Choices:
## Typography:
### Font:
- The font that was used was the standard Django font sans-serif
- In typography and lettering, a sans-serif, sans serif, gothic, or simply sans letterform is one that does not have extending features called "serifs" at the end of strokes. Sans-serif typefaces tend to have less stroke width variation than serif typefaces

### Colours:
- The colours that were used during this project were the standard bootstrap colours. 
- The main one that was used was the danger bootstrap font to represent the colour of a pokemon ball with the red and the white to give off the Pokemon ball vibe.
- ![Screenshot](/media/pokemon-ball.png)

- ![Screenshot](/media/bootstrap-colours.PNG)

# Features:
## Existing Features:

### Login and Register:
- Login Page is first thing to show up when opening the blog application as you cannot use it unless you have registered and logged in.
- ![Screenshot](/media/login-page.PNG)

- Register Page
- ![Screenshot](/media/register-page.PNG)

- Blog Core Page is the page you access after you have logged in where you can see all the blog posts that have been created and can also create your very own blog if you wish. The Pokemon Blog in the top left corner only appears if you are logged in! 
- ![Screenshot](/media/core-page.PNG)

- Blog Detail page is when after clicking a blog you can view and see more of that post and be able to comment on that post.
- ![Screenshot](/media/blog-detail-page.PNG)

- If you own the post then you will see buttons on the right where you can edit the blog post you made or be able to delete that post if you wish.
- ![Screenshot](/media/crud.PNG)

- You can edit the blog post you created and be able to change the title and description of that blog post.
- ![Screenshot](/media/crud-edit.PNG)

- You can delete or cancel the post if you don't want it to exist anymore or do not want to delete it.
- ![Screenshot](/media/crud-delete.PNG)

- On the Core page you can create a post that will appear to the right of the same page when you create a new blog with a title and description.
- ![Screenshot](/media/crud-create.PNG)

- You can click on the account page and change the username and email if you want to give you a bit more customization. You can confirm or cancel. 
- ![Screenshot](/media/edit-account-page.PNG)

- You can create a comment on a blog detail page and interact with others who also post on that blog post.
- ![Screenshot](/media/comment-page.PNG)



### Potential Features:

- I would like to be able to add images in the future and use Cloudinary to host those images.
- Comments can be upvoted and downvoted.
- Be able to have a section on core page where updated comments and posts are.
- show active users on page 
- links to social media

# Testing:
- Lighthouse score test:
- ![Screenshot](/media/lighthouse-report.PNG)

- CSS Validator:
- ![Screenshot](/media/css-report.PNG)

- HTML Validator:
- small div unused but couldn't find
- ![Screenshot](/media/html-report.PNG)

- Unittest and Coverage:
- I used Unittest to test the views, models and forms using django built in unnitest and screenshot the report for the test using coverage which helps give you an idea of where tests need to be made and views was the hardest thing to test. There is a htmlcov folder that was created from coverage that helps us view the report. 
Testing is hard but very important to make sure that all functions of your code work. 
- ![Screenshot](/media/coverage-report.PNG)

- Pep8
- Used PEP8 to follow to make sure the code is readable and has good naming functions to easily read it. I used https://pep8ci.herokuapp.com/# as a reference to see if any errors which I found none after making it inline with PEP8. 

- Testing was done across multiple viewports sizes to ensure responsiveness.

- Manual testing was constantly conducted to ensure successful deployment across the different platforms.

## Manual testing Python for the following functions listed below:

- Creating an account to enter and view site (Working)

- Entering details into form and submitting form (Working)

- Admin Panel that allows the Creating/Updating/Deleting of blog (Working)

- Allowing users to create/Edit blog/Delete blog (Working)

- Allow users to register and login (Working)

## Manual Testing For Javascript function
- Test Javascript script that the logged out danger message timeout after 5 seconds after logging out (working)
- ![Screenshot](/media/timeout-start-test.PNG)
- The message timesout after 5 seconds after logging out which indicates that our javascript is functioning as intended.

- ![Screenshot](/media/timeout-test.PNG)

## Automatic Testing For Javascript function
- I installed Jest inside my apllication but did not use it as I only used a small amount of Javascript overall to not use it.


# Responsiveness Test:
- Tested the responsive test which bootstrap helps with their templates to fit pages on any page and any screen where I manually tested using google chrome developement tools to test the responsiveness of my project.


## Browser Compatibility
- Google Chrome 
- ![Screenshot](/media/chrome-test.PNG)

- Mozilla Firefox 
- ![Screenshot](/media/firefox-test.PNG)

- Microsoft Edge 
- ![Screenshot](/media/microsoft-edge-test.PNG)




# Bugs
- Main bugs included that when I was not signed into account I could access core page so I had to use login_required decorator to fix that issue. (fixed)

- First attempt of Deployment had a big issue with admin page not displaying css so I had to collectstatic which solved the issue. 

- Testing views was tough as testing is something that takes time to get used too but that is something I want to improve further down the line. 

- Inside mobile view the hamburger menu does not display but can be clicked to view the login logout details

- Using main.css became an issue when trying to link the custom page as I had deployed the project and couldn't load static on page and was getting an error so I used CSS on the html page which I know is not the most opitmal solution as it should be linked in seperate file but in order for the scroll effect to work on comment page I linked on the html page as that is where my only custom css I used for this project. I have a custom CSS page with the same CSS but I couldn't link it for some bug reason but I want to make sure that it worked and I that you should always seperate your html and css in different files! 

- Small mistake in blog delete page where it should be blog delete instead of blog detail in the heading but couldn't change in time as I only saw it last second as I do not have time.  

# Technolgy used:
- Python - Provides the functionality for the site.
- HTML5 - Provides the content and structure for the website.
- CSS3 - Provides the styling for the website.
- JavaScript - Provides interactive elements of the website
- Django - A model-view-template framework
- Heroku - A cloud platform that the application is deployed to.
- Lighthouse - Used to test performance of site.
- HTML Validation - Used to validate HTML code
- CSS Validation - Used to validate CSS code
- Unittest - Django built in test


# Reference: 
- https://getbootstrap.com/docs/4.6/getting-started/introduction/ - Bootstrap 4.6 cdn
- https://getbootstrap.com/docs/4.6/components/navbar/ - navbar template
- https://getbootstrap.com/docs/4.6/components/modal/ - bootstrap Modal 
- https://getbootstrap.com/docs/4.6/components/collapse/#accordion-example - accordion collaspe
- https://wireframe.cc/ - Wireframes
- https://getbootstrap.com/docs/4.0/utilities/colors/ - bootstrap colours
- https://fontawesome.com/ - Font Awesome
- https://django-crispy-forms.readthedocs.io/en/latest/ - crispy forms 
- https://pypi.org/project/black/ - Used for keeping the python in check with guidlines of PEP8
- https://docs.djangoproject.com/en/4.2/topics/forms/ - Django Forms 
- https://websitemockupgenerator.com/ - MockUp generator 
- https://docs.djangoproject.com/en/4.2/topics/auth/default/ 
- https://validator.w3.org/ - html validator 
- https://jigsaw.w3.org/css-validator/ - CSS validator
- https://pep8ci.herokuapp.com/# - Code Institute Pep8 guideline 
- https://dev.to/balt1794/registration-page-using-usercreationform-django-part-2-2fg - UserCreationForm

# Deployment:

## Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:
Use the arrows below to drop down and view the steps

1. To begin with we need to create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.
- ![Screenshot](/media/code-institute-template.PNG)

<details><summary><b>Heroku Deployment - Step 1</b></summary>

Heroku Deployment Step 1

2. Fill in the needed details as stated in the screenshot below and then click 'Create Repository From Template'.

<details><summary><b>Heroku Deployment - Step 2</b></summary>

![Heroku Deployment Step 2]
</details><br />

3. When the repository creation is done click 'Gitpod' as stated in the screenshot below.
- ![Screenshot](/media/gitpod-button.PNG)

<details><summary><b>Heroku Deployment - Step 3</b></summary>

![Heroku Deployment Step 3]
</details><br />

4. Now it's time to install Django and the supporting libraries that are needed. Type the commands below to do this.

* ```pip3 install 'django<4' gunicorn```
* ```pip3 install 'dj_database_url psycopg2```
* ```pip3 install 'dj3-cloudinary-storage```

<details><summary><b>Heroku Deployment - Step 4</b></summary>

![Heroku Deployment Step 4]
</details><br />

5. When Django and the libraries are installed we need to create a requirements file.

* ```pip3 freeze --local > requirements.txt``` - This will create and add required libraries to requirements.txt

<details><summary><b>Heroku Deployment - Step 5</b></summary>

![Heroku Deployment Step 5]
</details><br />

6. Now it's time to create the project.

* ```django-admin startproject YOUR_PROJECT_NAME .``` - This will create your project

<details><summary><b>Heroku Deployment - Step 6</b></summary>

![Heroku Deployment Step 6]
</details><br />

7. When the project is created we can now create the application.

* ```python3 manage.py startapp APP_NAME``` - This will create your application

<details><summary><b>Heroku Deployment - Step 7</b></summary>

![Heroku Deployment Step 7]
</details><br />

8. We now need to add the application to settings.py

<details><summary><b>Heroku Deployment - Step 8</b></summary>

![Heroku Deployment Step 8]
</details><br />

8. Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.

* ```python3 manage.py migrate``` - This will migrate the changes
* ```python3 manage.py runserver``` - This runs the server. To test it, click the open browser button that will be visible after the command is run.

9. Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.

* Head on to [Heroku](https://www.heroku.com/) and sign in (or create an account if needed).

* In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.
- ![Screenshot](/media/create-new-app-heroku.PNG)

<details><summary><b>Heroku Step 09</b></summary>

![Heroku Step 9]
</details><br />

10. Now it's time to enter an application name that needs to be unique. When you have chosen the name, choose your region and click 'Create app".
- ![Screenshot](/media/create-app-heroku.PNG)

<details><summary><b>Heroku Step 10</b></summary>

![Heroku Step 10]
</details><br />

11. To add a database to the app you need to go to the resources tab ->> add-ons, search for 'Heroku Postgres' and add it.

<details><summary><b>Heroku Step 11</b></summary>

![Heroku Step 11]
</details><br />

12. Go to the settings tab and click on the reveal Config Vars button. Copy the text from DATABASE_URL (because we are going to need it in the next step).

<details><summary><b>Heroku Step 12</b></summary>

![Heroku Step 12]
</details><br />

13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

* ```import os``` - This imports the os library
* ```os.environ["DATABASE_URL_FROM HEROKU"]``` - This sets the environment variables.
* ```os.environ["SECRET_KEY"]``` - Here you can choose whatever secret key you want.

- ![Screenshot](/media/env-file.PNG)

<details><summary><b>Heroku Step 13</b></summary>

![Heroku Step 13]
</details><br />

14. Now we are going to head back to Heroku to add our secret key to config vars. See screenshot below.

- ![Screenshot](/media/secret-key.PNG)

<details><summary><b>Heroku Step 14</b></summary>

![Heroku Step 14]

15. Now we have some preparations to do connected to our environment and settings.py file. In the settings.py, add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

<details><summary><b>Heroku Step 15</b></summary>

![Heroku Step 15]
</details><br />

16. In the settings file, remove the insecure secret key and replace it with:
```SECRET_KEY = os.environ.get('SECRET_KEY')```

<details><summary><b>Heroku Step 16</b></summary>

![Heroku Step 16]
</details><br />

17. Now we need to comment out the old database setting in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).

<details><summary><b>Heroku Step 17 1/2</b></summary>

![Heroku Step 17]
</details><br />

Now, add the link to the DATABASE_URL that we added to the environment file earlier.

<details><summary><b>Heroku Step 17 2/2</b></summary>

![Heroku Step 17]
</details><br />

18. Save all your fields and migrate the changes.

```python3 manage.py migrate```

19. Now we are going to get our connection to Cloudinary connection working (this is were we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

```os.environ["CLOUDINARY_URL"] = "cloudinary://************************"```

21. Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.

<details><summary><b>Heroku Step 21</b></summary>

![Heroku Step 21]
</details><br />

22. Let's head back to our settings.py file on Gitpod. We now need to add our Cloudinary Libraries we installed earlier to the installed apps. Here it is important to get the order correct.

<details><summary><b>Heroku Step 22</b></summary>

![Heroku Step 22]

23. For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.

<details><summary><b>Heroku Step 23</b></summary>

![Heroku Step 23]
</details><br />

24. Hang in there, we have just a couple of steps left. Now it's time to link the file to the Heroku templates directory.

<details><summary><b>Heroku Step 24</b></summary>

![Heroku Step 24]
</details><br />

25. Let's change the templates directory to TEMPLATES_DIR in the teamplates array.

<details><summary><b>Heroku Step 25</b></summary>

![Heroku Step 25]
</details><br />

26. To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to which hosts that are allowed.

<details><summary><b>Heroku Step 26</b></summary>

![Heroku Step 26]
</details><br />

27. Now we just need to add some files to Gitpod.

* Create 3 folders in the top level directory: **media**, **static**, **templates**
* Create a file called **Procfile* and add the line ```web: gunicorn PROJ_NAME.wsgi?``` to it.d

28. Now you can save all the files and prepare for the first commit and push to Github by writing the lines below.

* ```git add .```
* ```git commit -m "Deployment Commit```
* ```git push```

29. Before moving on to the Heroku deployment we just need to add one more thing in the config vars. We need to add "PORT" in the KEY input field and "8000" in the VALUE field. If we don't add this there might be problems with the deployment.

30. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

31. Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!

<details><summary><b>Heroku Step 31</b></summary>

![Heroku Step 31]
</details><br />





## How To Fork The Repository On GitHub

It is possible to do a independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

<details><summary><b>Github Fork</b></summary>

![Fork](/media/fork-button.PNG)
</details><br />



## Cloning And Setting Up This Project

To clone and set up this project you need to follow the steps below.

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

<details><summary><b>Github Create Local Clone</b></summary>

![Clone]
![Clone](/media/clone-tab.PNG)
</details><br />

5. To be able to get the project to work you need to install the requirements. This can be done by using the command below:

* ```pip3 install -r requirements.txt``` - This command downloads and install all required dependencies that is stated in the requirements file.

6. The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

* ```python3 manage.py migrate``` - This will do the necessary migrations.
* ```python3 manage.py runserver``` - If everything i setup correctly the project is now live locally.

<details><summary><b>Setup env.py</b></summary>

![Clone](/media/env-file.PNG)
</details><br />


