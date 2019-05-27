```bash
////한성컴퓨터 X57K BossMonster Lv.74  에 Ubuntu18.04 설치

1. 바이오스 nVidai Grapic Disable 
2. Ubuntu 18.04 Server install
3. 바이오스 nVidai Grapic Enable 
4. nVidia Graphic dirver 자동 설치 
https://steemit.com/kr/@deep-root/ubuntu-cuda

sudo apt-get install ubuntu-drivers-common
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo ubuntu-drivers autoinstall
shutdown -h now  
nvidia-smi
-> 1050 잡혔는지 확인 

5. ubuntu desktop version 설치 
https://www.techrepublic.com/article/how-to-install-the-gnome-desktop-on-ubuntu-server-18-04/

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install tasksel -y
sudo tasksel

여기서 ubuntu desktop check 후 설치 . 


6. cuda 설치는 아래 링크 보고 
sudo apt install cuda-10-0
https://hiseon.me/2018/03/11/cuda-install/
```


```bash
우분투 서버 16.04.05 버전 설치 
설치하면 ubuntu desktop 설치 
커널 업데이트 하지 말것 무선랜 포기 
로스 설치 먼저   
터미널 버전 아닌 그래픽 화면에서 아래 nvidai 그래픽 카드, CUDA ,CuNN 설치
아래 사이트 대로 그래픽 버전에서 명령어로 설치 
https://hiseon.me/2018/02/17/install_nvidia_driver/

EIGEN3 는 ROS 설치시 /usr/include/eigen  폴더에 자동 설치 된다. 

\Eigen\src\Core\util\Macros.h 를 보면 버전 확인이 됨. 
기본  3.2.92 가 설치 되어있음. 
http://eigen.tuxfamily.org/index.php?title=Main_Page  에서 다운받아 설치 할 수 있음. 
3.3.5 가 현재 최신  
mkdir build
cd build
cmake ..
make
sudo make install
하지만 아래 폴더에 설치됨. 
/usr/local/include/eigen3
추가 알아내햐는 부분  
eigen3 기존것을 지우고 ros에서 지정한  /usr/include/eigen3 폴더에 설치하는 방법과 
기존것을 delete 가 아닌 방법으로 지우는 법을 알아야함. 

동일 상황에 있었던 두명의 PC설정 조사 


```

# pcsetting
```bash
hyunoklee@ubuntu:~$ nvidia-smi  
hyunoklee@ubuntu:~$ lsb_release -a  

No LSB modules are available.  
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.4 LTS
Release:	16.04
Codename:	xenial


apt-cache search linux-image
apt-get install linux-image-4.16.3-041603-generic


hyunoklee@ubuntu:~/123$ nvidia-smi
Fri Nov 16 15:11:31 2018       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 396.26                 Driver Version: 396.26                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1050    Off  | 00000000:01:00.0 Off |                  N/A |
| N/A   46C    P3    N/A /  N/A |    473MiB /  4040MiB |      2%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1170      G   /usr/lib/xorg/Xorg                           345MiB |
|    0      2404      G   compiz                                        86MiB |
|    0      2941      G   ...-token=24B52EEA099F262454147FD78AFB5692    39MiB |
+-----------------------------------------------------------------------------+
https://hiseon.me/2018/02/17/install_nvidia_driver/
'''
https://answers.ros.org/question/253181/howto-eigen-installation/
```bash
mkdir build
cd build
cmake ..
make
sudo make install

/usr/local/include/eigen3
/usr/include/eigen3
http://eigen.tuxfamily.org/index.php?title=Main_Page
\Eigen\src\Core\util\Macros.h

ubuntu 16.04.4->5 server defual version  3.2.92

EIGEN3_INCLUDE_DIR

include_directories
'''
