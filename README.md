# project-backend

***Before you start, please make sure you have installed python 3.8 or newer and docker***

Linux OS with building image from Dockerfile:
1. To initialize virtual enviroment first open terminal/cmd
2. Then change working directory to repository folder using cd command (For example "cd Cloud" would change your working directory to Cloud folder if it exists in your current folder).
3. Type into terminal "sudo apt install python3.10-venv" and hit enter
4. Type into terminal "python3 -m venv venv" and hit enter
5. Next enter command ". venv/bin/activate" and hit enter
6. Build docker image using command "docker build --tag flask-app ." (if you receive permission denied error then add sudo at the start of command).
7. Run docker container based on newly created image with "docker run --publish 8000:5000 flask-app"
9. Keep your cmd open and open your internet browser for example Firefox.
10. Copy url from terminal onto your web browser and hit enter.
11. You should see the Hello world message.
12. Add /hello to the ulr link to go to other endpoint
13. Enter your name and hit submit button
14. (Oprional) in the terminal use ctrl + c to close flask server and enter "pylint hello_world.py" - this will run static code test on python file.

