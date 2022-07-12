# Table of Contents 

1. [**Introduction**](#Introduction)
2. [**User Experience (UX)**](#User-Experience-(UX))
    * [Project goals](#Project-goals)
    * [Target audience](#Target-audience)
    * [User stories](#User-stories)
    * [Structure](#Structure)
    * [Design](#Design)

3. [**Features**](#Features)
    * [Existing Features](#Existing-Features)
    * [Features to be implemented in the future](#Features-to-be-implemented-in-the-future)

4. [**Technologies used**](#Technologies-used)

5. [**Deployment**](#Deployment)
    * [Deploying to Heroku](#Deploying-to-Heroku)
    * [Forking to GitHub Repository](#Forking-to-GitHub-Repository)
    * [Making a local clone](#Making-a-local-clone)

6. [**Testing**](#Testing)
    * [Testing Approach](#Testing-Approach)
    * [User stories testing from the UX section](#User-stories-testing-from-the-UX-section)
    * [Validator Testing](#Validator-Testing)
    * [Issues and Bugs](#Issues-and-Bugs)

7. [**Credits**](#Credits)

8. [**Acknowledgments**](#Acknowledgments)

9. [**Disclaimer**](#Disclaimer)

<br>

# MoodBox

[Live program](https://mood-box.herokuapp.com/)

![MoodBox image](#)


## Introduction
---

MoodBox is a digital self-care toolbox for anyone feeling anxious, low or overwhelmed. It’s full of bite-sized information on psychological principles that are known to reduce negative feelings and enhance well-being. The users can pop it open whenever they need a quick remedy, a healthy activity to distract their anxious mind or simply a reminder that they are not alone. 

In MoodBox, they can learn how others use different tools and techniques to calm down their anxiety and lift their mood. They will find practical tips and discover new coping strategies that they implement whenever they need them. They can also share your own insights and everyday strategies to help others.



## User Experience (UX)
---
### Project goals

* 
* 

### Target audience

* 
* 

### User stories:

**Site User:**

* As a site user, I can quickly learn what the site is about so I can decide if it offers something I want.
* As a site user, I can navigate the site so that I can find the page I want to go to.
* As a site user, I can view a paginated list of tools so I can select a new technique to try.
* As a site user, I can open a post so I can see more information and steps necessary to use it.
* As a site user, I can view the number of likes on a tool post so that I can decide if this helped others.
* As a site user, I can view the comments on tools so I can see even more tips and suggestions.
* As a site user, I can follow any links leading to extra resources.
* As a new user, I can sign up for an account so that I can start adding my own tools and comment and like content posted by others.

**Registered User:**

* As a registered user, I can sign into my account so that I can access my tools.
* As a registered user, I can sign out of my account when finished, so that I know I am signed out securely.
* As a registered user, I can create and share my own tools and tips for others users to view.
* As a registered user, I can edit my post so that I can correct or add to the previously recorded information.
* As a registered user, I can delete my post so that I can remove it from my records. 
* As a registered user, I can comment on other users' tips to interact with the content.
* As a registered user, I can like or unlike tips other users shared so I can interact with the content.
* As a registered user, I can add links to the posts so that I can point to an official resources.

**Site Admin:**

* As a site admin, I can create, view, update and delete posts so that I can manage my site content.
* As a site admin, I can approve user-created posts and comments so that I can manage the content of the site.
* As a site admin, I can remove users so that they will no longer be able to post unsuitable content.

### Structure:

* Flowchart

![Flowchart image]()

* Database Structure


### Design: 



## Features
---

### Existing Features

* 

### Features to be implemented in the future

Due to time constraints, I was unable to implement all planned features. In the future, I'd like to add the following:

* 
* 
* 
* 

## Technologies used
---

* [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) - to display and run the command line terminal in the browser
* [Lucidchart](https://www.lucidchart.com/) - to create the flowchart
* [Heroku](https://heroku.com/) - for presenting the deployed project
* [GitHub](https://github.com/) - for hosting the project code and version control 
* [Gitpod](https://gitpod.io/) - to write the code and push it to GitHub
* [PEP8 Online Validation Service](http://pep8online.com/) - to validate the code
* [Online-Spellcheck](https://www.online-spellcheck.com/) - to spellcheck the README

## Deployment
---
### Deploying to Heroku

[Deployed program on Heroku](https://mood-box.herokuapp.com/)

The project was developed in GitPod, committed to Git and pushed to GitHub. 
The site was deployed to Heroku with the following steps:

1. In GitPod, import the required dependencies to the requirements.txt file, using 
> pip3 freeze > requirements.txt
2. Git add, commit and push the saved changes to GitHub. Heroku will use this file to import the dependencies that are required.
3. Sign up and log in to [Heroku](https://heroku.com).
4. On the dashboard, click **New** in the top right-hand corner and select **Create New App**.
5. Select a *unique* name for your application and choose your region (Europe in my case).
6. Click **Create App**.
7. Navigate to the Settings tab (must be done before deploying code)
8. Go to section **Config Vars**, click button "Reveal Config Vars" and press "Add" button
9. 
10. 
11. 
12. Navigate to the Deploy tab and scroll down to **Deployment Method**.
13. Select GitHub as deployment method.
14. Enter the name of the repository you want to connect to and click **Connect**.
15. Select one of the deployment options - Automatic Deployments or Manual - to deploy the app.
16. Once successfully deployed, a **View** button will appear and take you to a mock terminal.


### Forking to GitHub Repository

You can create a fork (copy) of the repository. This allows you to experiment with the code without affecting the original project.

To fork the repository:

1. Log in to your [GitHub](https://github.com/) account 
2. On GitHub, navigate to the repository you want to fork
3. In the top right corner of the page, underneath your profile avatar, click **Fork**
4. You should now have a copy of the original repository in your GitHub account

### Making a local clone

You can clone your repository to create a local copy on your computer. Any changes made to the local copy will not affect the original project. To clone the **Winter Wedding** project, follow the steps below:

1. Log in to your [GitHub](https://github.com/) account and locate the [MoodBox repository](https://github.com/renatabiniek/moodbox)
2. In the repository, click on **Code** button located above all the project files
3. Under HTTPS, copy the link generated (https://github.com/renatabiniek/moodbox.git)
4. Open the terminal you're using, e.g. Gitpod
5. Change the current working directory to the location where you want the cloned directory created
6. Type ```git clone``` and then paste the URL you copied earlier:  
```git clone https://github.com/renatabiniek/moodbox.git``` 
7. Press **Enter** to create your local clone.

You can also refer to this [GitHub documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) for detailed instructions. 

## Testing
---

### Testing Approach

* 

*


* The program has been tested on various browsers on desktop and mobile:

  * Chrome
  * Mozila Firefox
  * Edge
  * Safari 


### User stories testing from the UX section

I tested the program considering the user stories from the UX section as well.

* 

  **Test result:**  



### Validator Testing



### Issues and Bugs

* 

### Credits

* 

* 

* 

* 

### Acknowledgments

Thank you to:

* 
* 
* 

### Disclaimer

*This program has been created for educational purposes only, as part of Code Institute’s Portfolio Project.*

[Back to top](#Table-of-Contents)