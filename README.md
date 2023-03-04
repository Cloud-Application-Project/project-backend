# project-backend

***Before you start, please make sure you have installed python 3.8 or newer***

Windows OS:
1. To initialize virtual enviroment first open terminal/cmd
2. Then change working directory to repository folder using cd command (For example "cd Cloud\app_folder" would change your working directory to app_folder inside Cloud folder if it exists in your current folder).
3. Type into cmd "python -m venv venv" and hit enter - this will create a virtual enviroment folder
4. Next activate virtual enviroment by typing into cmd "venv\Scripts\activate" then hit enter
5. Install dependecies with "pip install -r requirements.txt"
6. Type into CMD "SET FLASK_APP=hello_world.py" and hit enter
7. Now that your enviroment is activate you can run the application with command "flask run"
8. Keep your cmd open and open your internet browser for example Firefox.
9. Copy url from cmd onto your web browser and hit enter.
10. You should see the Hello world message.
11. Add /hello to the ulr link to go to other endpoint
12. Enter your name and hit submit button
13. (Oprional) in the cmd use ctrl + c to close flask server and enter "pylint hello_world.py" - this will run static code test on python file.

Linux OS:
1. To initialize virtual enviroment first open terminal/cmd
2. Then change working directory to repository folder using cd command (For example "cd Cloud" would change your working directory to Cloud folder if it exists in your current folder).
3. Type into terminal "sudo apt install python3.10-venv" and hit enter
4. Type into terminal "python3 -m venv venv" and hit enter
5. Next enter command ". venv/bin/activate" and hit enter
6. Install dependecies with "sudo pip install -r requirements.txt"
7. Type into CMD "FLASK_APP=hello_world.py" and hit enter
8. Now that your enviroment is activate you can run the application with command "flask run"
9. Keep your cmd open and open your internet browser for example Firefox.
10. Copy url from terminal onto your web browser and hit enter.
11. You should see the Hello world message.
12. Add /hello to the ulr link to go to other endpoint
13. Enter your name and hit submit button
14. (Oprional) in the terminal use ctrl + c to close flask server and enter "pylint hello_world.py" - this will run static code test on python file.

