sudo apt update
sudo apt-get install git -y
sudo apt-get install docker-compose -y
sudo apt-get install docker -y
sudo apt-get install default-libmysqlclient-dev -y
sleep 3
echo "Membuat Server Dalam Docker"
sudo docker build --tag capstone-server .
sudo docker-compose up -d
