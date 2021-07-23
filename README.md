# Flask_Full_Featured_BlogApp

1. Install 'pipenv' module using 'pip3 install pipenv'. Then run 'pipenv shell' on bash terminal in linux or mac and on cmd in windows to activate the pipenv virtual environment.

2. On the virtual environment install required dependencies using the requirements file using the 'pipenv install -r requirements.txt'.

3. Create the database tables using following command: Run a python interactive shell using 'python' command on your terminal and run the following command.

		>>> from flaskblogapp import create_app
		>>> app = create_app()
		>>> app.app_context().push()
		>>> from flaskblogapp import db, create_app
		>>> db.create_all(app=create_app())

4. Follow this video links to understand how to setup environment variables on different os.

windows:https://youtu.be/IolxqkL7cD8
linux/mac:https://youtu.be/5iWhQWVXosU (if .bash_profile doesn't work for you on linux distros,use .bashrc file for storing variables.)

Thanks to Corey Schafer(https://www.youtube.com/c/Coreyms) for this tutorial.

