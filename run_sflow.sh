
wget https://inmon.com/products/sFlow-RT/sflow-rt.tar.gz

tar -xvzf sflow-rt.tar.gz

cd ~/sflow-rt

sflow agent-ip 10.10.10.1

sudo bash start.sh &>> sflow_out.txt
