# capstoneAPI
Build and running the program
1. setup the credential json for GCP Bucket in credential-key.json
2. setup the correct configuration of GCP project in utils folder
3. running the file "build.sh"
4. setup the mysql database on "localhost:3306"
5. add the database with name = "capstone_db"
6. import the SQL query for generating the database table in directory "functions/dbcapstone.sql"
7. create mongo database on "localhost:2017" with name "capstone_db"
8. import the collection on directory "utils/information" to mongodb
9. restart the docker server container with "sudo docker container restart server"
10. all service will run properly 
