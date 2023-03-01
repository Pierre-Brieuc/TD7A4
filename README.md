# TD7A4
TD7 - Cloud Computing

If you want to use Docker compose, you have to follow these steps:
* 1 - Be sure to be in the /TD7A4/Using_Docker_Compose directory
* 2 - In a terminal, enter: docker-compose up --build
* 3 - Then, go on the port 5000 of your localhost and see what happens

Else if you don't want to use Docker compose, you have to follow these steps:
* 1 - Be sure to be in the /TD7A4 directory
* 2 - In a terminal, enter: $ docker build . -t python-app-td6
* 3 - In a terminal, enter: $ docker run -p 5000:5000 -v ~/path/to/your/directory:/usr/src/app python-app-td6
* 4 - Then, go on the port 5000 of your localhost and see what happens
