cd ~
sudo apt-get update
sudo apt-get install -y vim x11vnc
sudo apt-get install -y cmake unzip ntp joystick avahi-utils jq pkg-config build-essential git i2c-tools 
sudo apt-get install -y python3-virtualenv python3-pandas gfortran libjpeg-dev libopenjp2-7-dev libtiff-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libavcodec-dev libavformat-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev libtiff5-dev libopenblas-dev libhdf5-serial-dev python3-dev python3-pip libpng-dev 
sudo apt-get install -y python3-opencv 
sudo pip3 install -U numpy 
sudo apt-get install -y festival vlc gstreamer1.0-tools libpthread-stubs0-dev 
sudo apt-get install -y python3-numpy python3-matplotlib python3-scipy 
sudo pip3 install imutils gtts requests 
sudo apt-get install -y libjasper-dev libpng12-dev 
sudo apt-get -y install sox flac ntpdate swig3.0 python-pyaudio portaudio19-dev libssl-dev espeak mpg123 python-pip python-dev python-virtualenv libffi-dev 
sudo apt-get -y install libpython3-all-dev libttspico-data python3-pyaudio python3-all python3-all-dev python3-pysocks libttspico-utils libttspico0 
sudo pip3 install -U setuptools wheel SpeechRecognition 
sudo pip3 install -U cairocffi python-vlc youtube_dl 
sudo pip3 install dialogflow 
wget https://github.com/opencv/opencv_contrib/archive/4.5.1.tar.gz -O opencv_contrib-4.5.1.tar.gz 
tar zxvf opencv_contrib-4.5.1.tar.gz 
wget https://github.com/opencv/opencv/archive/4.5.1.tar.gz 
tar zxvf 4.5.1.tar.gz 
cd opencv-4.5.1 
mkdir build 
cd build 
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=/home/pi/opencv_contrib-4.5.1/modules \
    -D BUILD_EXAMPLES=ON \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFP3=ON .. 
time make -j4 VERBOSE=1 
sudo make install
cd ~
python3 -m virtualenv -p python3 env --system-site-packages
echo "source ~/env/bin/activate" >> ~/.bashrc
source ~/.bashrc
wget https://www.piwheels.org/simple/tensorflow/tensorflow-1.13.1-cp37-none-linux_armv7l.whl
pip3 install tensorflow-1.13.1-cp37-none-linux_armv7l.whl
