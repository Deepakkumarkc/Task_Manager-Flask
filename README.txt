1.Open Visual Studio Code

2.Open Terminal in VS Code

3.Install Python in system
	-$ sudo apt update
	-$ sudo apt install python3
	-$ python3 --version
	-$ sudo /opt/lampp/lampp start  # Start the xampp
	-$ sudo /opt/lampp/lampp stop 	# Stop the xampp

4.Make Environment Setup It is use to make sepereate environment from oru computer
	-$ pip3 install virtualenv
	-$ sudo apt install python3-virtualenv
	-$ virtualenv env

5.Now env file create in current file path

6.Now Activate the env 
	-$ source env/bin/activate [only for linux]

7.Then install Flask 
	-$ pip3 install flask flask-sqlalchemy


8.After create the code 
	-$ source  env/bin/activate  ## Activate the env in vs code
	-$ python3
	-$ db.create_all()
	-$ exit()
