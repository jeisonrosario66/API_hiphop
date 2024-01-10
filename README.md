
# API_hiphop

* It is a project with the objective of collect and organize much data the music RAP to expose it 

**Only developing local for now**
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

`HOST`

`USER`

`PASSWORD`

`DATA`
## API Reference
* All methods return the data in the format 'json'

#### Get all items
* This method makes a query and return all items the database

```http
  GET /api/artists
```
![captura](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/742f944c-61c4-4d7c-a005-76c9402fb2e2)

#### Get item
* This method makes a query and return an only item the database
```http
  GET /api/artist/${key}
```
![captura](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/dacf04ca-9618-4b6f-83e5-e75872ad6ec4)

#### Post item
* This method makes a query of post an item a the database, the dataset (data) must be in formato 'json'

```http
  POST /api/artist/${data}
```
![captura](https://github.com/jeisonrosario66/API_hiphop/assets/96961824/a183bafa-717c-47d2-85d9-a285b16bb518)


### Delete item

* This method makes a query of delete a item
```http
  POST /api/artist/${key}
```
