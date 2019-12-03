# Installation File

## System Requirements

In order to use the Spicify web application the user must have a Spotify account. Since we are using the Spotify api to search and gather music, if the user does not have Spotify the playlist will not be able to be created.




## Instructions to build and install

### Prerequisites

Python must be installed in order to run Spicify. Python can be installed here. We used python 3.7.4 when developing our project.
https://www.python.org/downloads/


### Installing
The Spicify team used Visual Studio Code IDE to build our project. To download VSCode on your machine visit the link below.
https://code.visualstudio.com/

Once VSCode is downloaded we followed an installation guide. Spicify was built using the Django framework in a virtual enviornment.
How to install django and the virtual enviornment is linked below.
https://code.visualstudio.com/docs/python/tutorial-django

It is very important to set the interpreter to "Python Interpreter" and then select "Python 3.7.4 32-bit" In your VSCode django project the interpreter can be selected by the command:**Ctrl+Shift+P**

Next the Spotify Api (Spotipy) package needs to be installed. Be sure to install this inside your enviornment or else you will receive an error "module not found". To install Spotipy you can use the command: **pip install spotipy**

The pip command is not always the most updated version of Spotipy available. We also used the following command to install Spotipy to ensure we were using the latest version and had access to all of Spotipy's functionality: **pip install git+https://github.com/plamere/spotipy.git --upgrade**
          
Once all of your project files have been downloaded into your enviornment the project can be ran using the command: **python manage.py runserver**

Other pip installations you need to run in the VS Code command line
**pip install pillow**
