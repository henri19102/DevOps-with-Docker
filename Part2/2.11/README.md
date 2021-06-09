# Exercise 2.11

My development environment with docker:

My project had Node.js backend and React frontend. Those located in separate folders, so I had to make two dockerfiles to build two images. I made docker-compose.yml file, which builds two containers for backend and frontend. With volumes I shared the project from containers to locally. Then I was able to edit the code locally and see changes in browser, while my containers were running.