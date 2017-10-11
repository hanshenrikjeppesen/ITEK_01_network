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

When you have the GitHub repository, you can make a new file and call it a name for instance `test.py` [see this for info]( https://help.github.com/articles/creating-new-files/)

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

![PyCharm configure](https://hanshenrikjeppesen.github.io/ITEK_01_network/doc/images/PyCharm_clone.jpg)











