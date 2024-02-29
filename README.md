
# API_hiphop

* It is a project with the objective of collect and organize much data the music RAP to expose it. In this first stage will show only data about artist

**App in production state**

**LINK:** **http://jeisonrosariodev.pythonanywhere.com/**
## Requirements 

#### DataBase

* Principal requirement to run the app is to have a database, this needs a specific structure

```SQL
CREATE TABLE `artist_table` (
   `artist_key` int NOT NULL AUTO_INCREMENT,
   `artist_aka` varchar(45) NOT NULL,
   `artist_name` varchar(45) DEFAULT NULL,
   `artist_dateborn` date DEFAULT NULL,
   `artist_deathdate` date DEFAULT NULL,
   `artist_country` varchar(45) DEFAULT NULL,
   PRIMARY KEY (`artist_key`),
   UNIQUE KEY `artist_key_UNIQUE` (`artist_key`),
   UNIQUE KEY `artist_aka_UNIQUE` (`artist_aka`)
 )
```

#### Environment Variables
To run this project, you will need to add the following environment variables to your `.env` file

```
HOST=hostname
USER=user
PASSWORD=pass
DATA=database_name
```
## Front end of the app
* This screen show the data artists in table format, each row in it has in click event, when pressed on a row make request to server and it return a new template with the data required

![1](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/90d26d66-173f-484c-af90-fa121822154a)

#### Get only artist
* Here show the data required and besides functions for modified the data as required

![2](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/94425d6e-8b53-489f-9c01-ab72953922c1)


![3](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/3aa84bb4-c773-4637-a91e-4f9f1c5ba294)

* You can too to access from the url, for example: 
```http
  /artist/artist_name
```
```http
  /add_artist
```

#### Add new artist
* This screen make the "insert into". Through of "output" windows you will can se the request state
![4](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/4dd325b0-d254-4b59-907e-e17dd612c736)

* "output" too has a method of verify avoid entities duplicate on the database

![5](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/94f08f08-4db8-4af5-a712-9ed07f3c75c4)
