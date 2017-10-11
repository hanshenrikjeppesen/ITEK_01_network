# PyCharm and GitHub
-with Raspberry Pi projects

## Introduction

[PyCharm](https://www.jetbrains.com/pycharm/download/){:target="_blank"} Is a Lightweight IDE for Python & Scientific development.

[GitHub](https://github.com/){:target="_blank"} is a version control system for tracking changes in computer files and coordinating work on those files among multiple people.(Wiki)

Try looking at this page for more info ["What Is GitHub, and What Is It Used For?"](https://www.howtogeek.com/180167/htg-explains-what-is-github-and-what-do-geeks-use-it-for/)

If you combine these two products / services, you will get a more fluent workflow developing and testing code on your raspberry pi. Hopefully this small guide will get you started. If you run into problems or have ideas for changes, please contact me:

______
For comments and suggestions or more information please contact me:

[eMail](mailto:hans@eaaa.dk)

[Linkedin](https://www.linkedin.com/in/hansjeppesen/){:target="_blank"}

______

## Installation

- First of course we must install `PyCharm` on Windows, Linux or MacOS [download](https://www.jetbrains.com/pycharm/download/)
- We also need to install `Git` - try looking at this [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- If you don’t already have a `GitHub account`, you will need to setup a user account [link](https://github.com/)
- You need to do a Git installation on the raspberry as well

## Step 1 - Git(Hub) setup

Let’s take it one step at a time. When you have installed PyCharm and Git on your computer and you have made a user account on GitHub, we are almost ready to go.

You will need to make a repository in GitHub for your project [see this for info](https://help.github.com/articles/creating-a-new-repository/)

When you have the GitHub repository, you can make a new file and call it a name for instance `helloWorld.py` [see this for info]( https://help.github.com/articles/creating-new-files/) and type in a simple python program:

```python
# a simple python script
print('Hello World!')

```
## Step 2 PyCharm Setup

Now we are almost ready to open `PyCharm` and work on the file `test.py`.
![PyCharm VCS](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/PyCharm_VCS.png)

But first we need to configure PyCharm with the information of our GitHub account, so click on Configure down in the right corner (see screenshot):

![PyCharm configure](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/PyCharm_configure.jpg)

1. Find the “Version Control” and choose “GitHub”
1. Set Auth Type to Password and type in your username (login) and Password for the GitHub account that you have made. Click on Apply and OK. 

![PyCharm configure](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/PyCharm_configure_github.jpg)

## Step 3 PyCharm Clone Repository

Now that we have a connection to GitHub (you can test it in Settings) we are now able to `Clone` that repository to a local project in PyCharm and keep a local version of the code.

![PyCharm configure](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/PyCharm_git_clone.jpg)

1. Choose the repository that you want to clone
1. `Test` the connection (hopefully it will work)
1. If you want to change the `Parent Directory` and/or `Directory Name` locally, you can do it here
1. Finally Click `Clone`

![PyCharm configure](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/PyCharm_git_yes.jpg)

**YES! -  NOW LET THE FUN BEGIN**

## Step 4 Raspberry Pi

Now let us turn to the Raspberry Pi and get it up and running. We will need to install git on it before we can `Clone`, `Commit`, and `Push/Pull` code to and from the Raspberry. So let’s do that right away. Connect to the Raspberry Pi using SSH.

Prepare for install and do a update

`sudo apt-get update`

Install Git on the Raspberry Pi

`sudo apt-get install git`

We need to let git know who we are, so lets give the config file som basic information

`git config --global user.email "your@email"`

`git config --global user.name "userNameOnGitHub"`

The terms, `Clone`, `Commit`, and `Push/Pull` is the terminology that git uses and [Oliver Steele](http://blog.osteele.com/2008/05/my-git-workflow/) made this complex but useful diagram for Git Data transport:

![Git data transport](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/git-transport.png)

You don't need to understand and explain the diagram, but it gives you a overview of where data is and where it goes when you issue different commands. So let’s start by clone the GitHub repository “Hello-World” to our Raspberry Pi.

When you `Clone` a repository you will get a directory on the Raspberry Pi with the name of the Repository. 
So, therefore, let's start by placing ourselves in the folder structure we want to create a Repository-folder from and then type:

Now you will need the URL for the Repository. You can find it here:

![Git find URL](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/git_repo_URL_new.png)

In the case of my "Hello World" Repository with my "helloWorld.py" file the URL is:
`https://github.com/hanshenrikjeppesen/Hello-World.git`

Lets clone a repository:

`git clone https://github.com/hanshenrikjeppesen/Hello-World.git`

Hopefully you would get something like:

![Git clone rasp](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/git_clone_rasp.png)

Do a `ls` and see if the directory is there.

![Git ls rasp](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/git_ls_rasp.png)

![missing](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/rasp_python_first.png)

![missing](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/pycharm_change_code.png)

![missing](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/pycharm_commit_push.png)

![missing](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/rasp_push_succes.png)

![missing](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/rasp_git_pull_run_code.png)


























