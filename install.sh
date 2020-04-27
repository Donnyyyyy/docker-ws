sudo apt install redis

git clone <url>
cd ws
pip3 install -r requirements.txt

python server.py &
rq worker &