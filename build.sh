sudo apt-get install git -y
sudo apt-get install docker -y
sudo apt-get install default-libmysqlclient-dev -y
source ./capenv/bin/activate
echo "Install Dependencies"
sleep 10
pip install -r requirements.txt
echo "Menjalankan Server"
python3 main.py
