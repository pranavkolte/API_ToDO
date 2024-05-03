# API_ToDO

Documentation link :https://paper-father-7d5.notion.site/To-Do-API-91026a7e662a4ec79d92fcab92600a3a


##Run using 
## create new database 
![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)

## import database 
![alt text](image-12.png)
![alt text](image-13.png)


Make sure your docker engine is turned on
run ```docker-compose up --build```
open terminal run ```docker contanier ls```
![alt text](image-14.png)

run ```docker inspect <sql_image_name>```

![alt text](image-15.png)

copy IP address 

![alt text](image-16.png)

got to app/database/db_config
replace host with current IP

![alt text](image-17.png)

You are good to go 

## Bearer token
![alt text](image-8.png)

## /signup
![alt text](image.png)

## UID/{email}
![alt text](image-1.png)

## task/create/
![alt text](image-2.png)


## task/all/{UID}
![alt text](image-3.png)

## task/delete/{TID}
![alt text](image-4.png)

## task/update/
![alt text](image-5.png)


## database snapshots
![alt text](image-6.png)
![alt text](image-7.png)
