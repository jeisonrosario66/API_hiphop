
# API_hiphop

* API_hip_hop is a project with the objective of collect and organize much data the music RAP to expose it. In this first stage will show only data about artist

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

![1](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/6c2c7a37-0474-40d4-8e1b-82ee96e633f4)

#### Get only artist
* Here show the data required and besides functions for modified the data as required

![2](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/75adf39c-e02a-44bf-b89c-af9d8e788a7c)



![3](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/94bf468f-a932-43f0-9f69-d2512a2c1e06)

* You can too to access from the url, for example: 
```http
  /artist/artist_name
```
```http
  /add_artist
```

#### Add new artist
* This screen make the "insert into". Through of "output" windows you will can se the request state
![4](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/7c41c9d5-3a96-40ab-9335-95a2d69cf734)

* "output" too has a method of verify avoid entities duplicate on the database

![5](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/55fcfdc7-899f-4443-a781-e808a817efda)
