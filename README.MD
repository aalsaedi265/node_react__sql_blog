PIP3 INSTALL FLASK, FLASK-SQLALCHEMY, mysql client, marshmallow, marshmallow sql alchemy

sudo apt-get install libmysqlclient-dev  if mysql client installtion give you troubel

marshamllow deals with the serilization/desrilations library so back and front talk to each other 

mysql client sql shell editing capabilites

in terminal if type PYTHON3 will enter the python terminal 

aboe was python suff


-------------------------------STARET HERE-----------------------------

npm init -y
 npm install express mysql nodemon



npm link --force mysql
npm i mysql-server
service mysql start  to start   also instead of service you can use systemctl

sudo /etc/init.d/mysql start  this fixed broken connection; be usre to always test a new connection when builfing using """""+"""""


https://www.tutorialrepublic.com/faq/how-to-start-stop-mysql-server-on-ubuntu.php





-- will teach how to install and use these commands
-- https://www.youtube.com/watch?v=7S_tz1z_5bA

how to insert

INSERT INTO `testPlease_work`.`books` (`id`, `title`, `description`, `cover`) VALUES ('1', 'Steall Ball Run', 'Part 7 and most epic of the jojo Bizar adventure', 'It is aswwom');


Error: listen EADDRINUSE: address already in use :::3306   Emitted 'error' event on Server instance at:

kill it with

sudo lsof -i :3306

sudo kill pid

or change it with 

port = 3307