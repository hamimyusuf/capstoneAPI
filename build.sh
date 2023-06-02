sudo apt update
sudo apt-get install git -y
sudo apt-get install docker-compose -y
sudo apt-get install docker -y
sudo apt-get install default-libmysqlclient-dev -y
source ./capenv/bin/activate
echo "Install Dependencies"
sleep 3
pip install -r requirements.txt
echo "Membuat Server Dalam Docker"
sudo docker build --tag capstone-server .
sudo docker-compose up -d
