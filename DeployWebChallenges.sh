#!/bin/bash 

# Everything needs to be installed properly for this to work! This just turns everything on. 
cd ./Library/API/
python3 api.py &

sudo service mysql start
cd ~/SMC2/korean-food/client
yarn start &

cd ~/SMC2/korean-food/react-backend
yarn start &

cd ~/SMC2/side_channel/
python deploy.py

cd ~/SMC2/first_sqli/frontend
python3 -m  http.server 8181 &
cd ../backend
python3 api.py &

cd ~/SMC2/easy_redirect
python3 redirect_fun.py &