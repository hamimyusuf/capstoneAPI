source ./capenv/bin/activate
echo "Install Dependencies"
sleep 10
pip install -r requirements.txt
echo "Menjalankan Server"
python3 main.py