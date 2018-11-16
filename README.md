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

'''
