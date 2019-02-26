mkdir drivers
cd drivers
wget https://chromedriver.storage.googleapis.com/72.0.3626.69/chromedriver_linux64.zip
unzip *
export PATH=$(pwd):$PATH
