```bash
////한성컴퓨터 X57K BossMonster Lv.74  에 ubuntu 16.04 load tl 
UEIF 바이오스 setting disable 해야 켜짐 
```
```bash
////한성컴퓨터 X57K BossMonster Lv.74  에 Ubuntu18.04 설치

1. 바이오스 nVidia Grapic Disable 
2. Ubuntu 18.04 Server install
3. 바이오스 nVidia Grapic Enable 
4. 터미널서 nVidia Graphic dirver 자동 설치 
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

////////hallyway  정상 동작 

INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 1000. Time Elapsed: 145.093 s Mean Reward: -0.443. Std of Reward: 1.052. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 2000. Time Elapsed: 636.589 s Mean Reward: -0.370. Std of Reward: 0.944. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 3000. Time Elapsed: 782.178 s Mean Reward: -0.353. Std of Reward: 1.196. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 4000. Time Elapsed: 930.389 s Mean Reward: -0.238. Std of Reward: 1.280. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 5000. Time Elapsed: 1076.734 s Mean Reward: -0.114. Std of Reward: 1.124. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 6000. Time Elapsed: 1221.032 s Mean Reward: -0.269. Std of Reward: 1.361. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 7000. Time Elapsed: 1367.102 s Mean Reward: -0.343. Std of Reward: 1.143. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 8000. Time Elapsed: 1511.823 s Mean Reward: -0.359. Std of Reward: 1.043. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 9000. Time Elapsed: 1657.246 s Mean Reward: -0.192. Std of Reward: 1.307. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 10000. Time Elapsed: 1803.499 s Mean Reward: -0.325. Std of Reward: 1.027. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 11000. Time Elapsed: 1949.638 s Mean Reward: -0.232. Std of Reward: 1.374. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 12000. Time Elapsed: 2095.420 s Mean Reward: -0.064. Std of Reward: 1.358. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 13000. Time Elapsed: 2242.408 s Mean Reward: -0.088. Std of Reward: 1.352. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 14000. Time Elapsed: 2388.856 s Mean Reward: 0.035. Std of Reward: 1.447. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 15000. Time Elapsed: 2534.672 s Mean Reward: -0.307. Std of Reward: 1.335. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 16000. Time Elapsed: 2682.374 s Mean Reward: -0.258. Std of Reward: 1.331. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 17000. Time Elapsed: 2828.560 s Mean Reward: -0.170. Std of Reward: 1.114. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 18000. Time Elapsed: 2972.646 s Mean Reward: -0.358. Std of Reward: 1.106. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 19000. Time Elapsed: 3116.352 s Mean Reward: -0.367. Std of Reward: 0.956. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 20000. Time Elapsed: 3263.363 s Mean Reward: -0.133. Std of Reward: 1.161. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 21000. Time Elapsed: 3411.022 s Mean Reward: -0.224. Std of Reward: 1.229. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 22000. Time Elapsed: 3556.604 s Mean Reward: -0.101. Std of Reward: 1.290. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 23000. Time Elapsed: 3703.600 s Mean Reward: -0.145. Std of Reward: 1.355. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 24000. Time Elapsed: 3850.201 s Mean Reward: 0.190. Std of Reward: 1.527. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 25000. Time Elapsed: 3996.467 s Mean Reward: -0.108. Std of Reward: 1.431. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 26000. Time Elapsed: 4144.490 s Mean Reward: -0.106. Std of Reward: 1.422. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 27000. Time Elapsed: 4290.619 s Mean Reward: -0.114. Std of Reward: 1.356. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 28000. Time Elapsed: 4435.413 s Mean Reward: 0.001. Std of Reward: 1.390. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 29000. Time Elapsed: 4580.552 s Mean Reward: 0.110. Std of Reward: 1.569. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 30000. Time Elapsed: 4726.860 s Mean Reward: 0.189. Std of Reward: 1.655. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 31000. Time Elapsed: 4873.884 s Mean Reward: -0.077. Std of Reward: 1.310. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 32000. Time Elapsed: 5020.903 s Mean Reward: 0.241. Std of Reward: 1.545. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 33000. Time Elapsed: 5167.665 s Mean Reward: 0.057. Std of Reward: 1.390. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 34000. Time Elapsed: 5314.304 s Mean Reward: 0.089. Std of Reward: 1.313. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 35000. Time Elapsed: 5460.638 s Mean Reward: 0.579. Std of Reward: 1.604. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 36000. Time Elapsed: 5607.778 s Mean Reward: 0.540. Std of Reward: 1.701. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 37000. Time Elapsed: 5754.426 s Mean Reward: 0.386. Std of Reward: 1.596. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 38000. Time Elapsed: 5902.369 s Mean Reward: 0.327. Std of Reward: 1.277. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 39000. Time Elapsed: 6051.028 s Mean Reward: 0.222. Std of Reward: 1.502. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 40000. Time Elapsed: 6197.702 s Mean Reward: 0.286. Std of Reward: 1.407. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 41000. Time Elapsed: 6345.475 s Mean Reward: 0.499. Std of Reward: 1.499. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 42000. Time Elapsed: 6493.415 s Mean Reward: 0.447. Std of Reward: 1.669. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 43000. Time Elapsed: 6642.706 s Mean Reward: 0.907. Std of Reward: 1.720. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 44000. Time Elapsed: 6790.831 s Mean Reward: 1.144. Std of Reward: 2.360. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 45000. Time Elapsed: 6939.638 s Mean Reward: 0.649. Std of Reward: 1.871. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 46000. Time Elapsed: 7086.943 s Mean Reward: 0.652. Std of Reward: 1.715. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 47000. Time Elapsed: 7235.296 s Mean Reward: 0.992. Std of Reward: 1.513. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 48000. Time Elapsed: 7384.404 s Mean Reward: 0.658. Std of Reward: 1.636. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 49000. Time Elapsed: 7531.321 s Mean Reward: 0.651. Std of Reward: 1.476. Training.
INFO:mlagents.envs:Saved Model
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 50000. Time Elapsed: 7678.523 s Mean Reward: 1.120. Std of Reward: 1.706. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 51000. Time Elapsed: 7825.949 s Mean Reward: 0.862. Std of Reward: 1.758. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 52000. Time Elapsed: 7974.443 s Mean Reward: 0.863. Std of Reward: 1.650. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 53000. Time Elapsed: 8120.713 s Mean Reward: 0.861. Std of Reward: 1.869. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 54000. Time Elapsed: 8268.855 s Mean Reward: 1.221. Std of Reward: 2.023. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 55000. Time Elapsed: 8418.343 s Mean Reward: 0.923. Std of Reward: 1.880. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 56000. Time Elapsed: 8566.653 s Mean Reward: 1.128. Std of Reward: 1.722. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 57000. Time Elapsed: 8713.625 s Mean Reward: 1.954. Std of Reward: 2.102. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 58000. Time Elapsed: 8863.258 s Mean Reward: 1.916. Std of Reward: 2.089. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 59000. Time Elapsed: 9012.625 s Mean Reward: 1.780. Std of Reward: 2.025. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 60000. Time Elapsed: 9159.432 s Mean Reward: 1.780. Std of Reward: 2.088. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 61000. Time Elapsed: 9306.248 s Mean Reward: 1.811. Std of Reward: 1.997. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 62000. Time Elapsed: 9453.282 s Mean Reward: 1.556. Std of Reward: 2.099. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 63000. Time Elapsed: 9600.947 s Mean Reward: 1.727. Std of Reward: 2.133. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 64000. Time Elapsed: 9747.438 s Mean Reward: 1.734. Std of Reward: 2.080. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 65000. Time Elapsed: 9893.113 s Mean Reward: 1.445. Std of Reward: 1.851. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 66000. Time Elapsed: 10039.606 s Mean Reward: 2.061. Std of Reward: 1.881. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 67000. Time Elapsed: 10188.973 s Mean Reward: 1.905. Std of Reward: 2.133. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 68000. Time Elapsed: 10335.222 s Mean Reward: 2.057. Std of Reward: 2.121. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 69000. Time Elapsed: 10482.380 s Mean Reward: 2.517. Std of Reward: 2.265. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 70000. Time Elapsed: 10629.253 s Mean Reward: 2.054. Std of Reward: 2.443. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 71000. Time Elapsed: 10775.843 s Mean Reward: 1.970. Std of Reward: 1.974. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 72000. Time Elapsed: 10922.685 s Mean Reward: 2.199. Std of Reward: 2.208. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 73000. Time Elapsed: 11070.071 s Mean Reward: 2.216. Std of Reward: 2.101. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 74000. Time Elapsed: 11218.908 s Mean Reward: 2.561. Std of Reward: 2.121. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 75000. Time Elapsed: 11367.076 s Mean Reward: 2.413. Std of Reward: 2.144. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 76000. Time Elapsed: 11513.934 s Mean Reward: 2.470. Std of Reward: 2.180. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 77000. Time Elapsed: 11661.321 s Mean Reward: 2.365. Std of Reward: 2.108. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 78000. Time Elapsed: 11808.070 s Mean Reward: 2.452. Std of Reward: 2.016. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 79000. Time Elapsed: 11953.806 s Mean Reward: 2.966. Std of Reward: 2.359. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 80000. Time Elapsed: 12104.024 s Mean Reward: 2.346. Std of Reward: 2.088. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 81000. Time Elapsed: 12256.404 s Mean Reward: 2.946. Std of Reward: 2.193. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 82000. Time Elapsed: 12407.461 s Mean Reward: 2.489. Std of Reward: 2.147. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 83000. Time Elapsed: 12557.151 s Mean Reward: 2.906. Std of Reward: 2.444. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 84000. Time Elapsed: 12705.295 s Mean Reward: 2.397. Std of Reward: 2.109. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 85000. Time Elapsed: 12853.937 s Mean Reward: 2.940. Std of Reward: 1.925. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 86000. Time Elapsed: 13003.153 s Mean Reward: 2.860. Std of Reward: 2.382. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 87000. Time Elapsed: 13153.964 s Mean Reward: 3.437. Std of Reward: 2.554. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 88000. Time Elapsed: 13303.237 s Mean Reward: 2.640. Std of Reward: 1.934. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 89000. Time Elapsed: 13450.670 s Mean Reward: 2.785. Std of Reward: 2.683. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 90000. Time Elapsed: 13597.834 s Mean Reward: 3.518. Std of Reward: 2.049. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 91000. Time Elapsed: 13745.217 s Mean Reward: 3.538. Std of Reward: 2.365. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 92000. Time Elapsed: 13892.942 s Mean Reward: 3.427. Std of Reward: 2.285. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 93000. Time Elapsed: 14039.155 s Mean Reward: 3.497. Std of Reward: 2.138. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 94000. Time Elapsed: 14185.915 s Mean Reward: 2.930. Std of Reward: 2.158. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 95000. Time Elapsed: 14334.438 s Mean Reward: 3.399. Std of Reward: 2.786. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 96000. Time Elapsed: 14481.218 s Mean Reward: 3.391. Std of Reward: 1.989. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 97000. Time Elapsed: 14628.312 s Mean Reward: 2.961. Std of Reward: 1.984. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 98000. Time Elapsed: 14776.853 s Mean Reward: 3.175. Std of Reward: 2.225. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 99000. Time Elapsed: 14923.606 s Mean Reward: 3.509. Std of Reward: 1.745. Training.
INFO:mlagents.envs:Saved Model
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 100000. Time Elapsed: 15072.383 s Mean Reward: 3.854. Std of Reward: 2.383. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 101000. Time Elapsed: 15220.659 s Mean Reward: 4.209. Std of Reward: 2.398. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 102000. Time Elapsed: 15367.745 s Mean Reward: 3.558. Std of Reward: 1.849. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 103000. Time Elapsed: 15514.871 s Mean Reward: 3.948. Std of Reward: 2.416. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 104000. Time Elapsed: 15660.990 s Mean Reward: 4.257. Std of Reward: 2.117. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 105000. Time Elapsed: 15807.442 s Mean Reward: 4.043. Std of Reward: 2.257. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 106000. Time Elapsed: 15954.731 s Mean Reward: 3.355. Std of Reward: 2.100. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 107000. Time Elapsed: 16101.925 s Mean Reward: 4.064. Std of Reward: 2.137. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 108000. Time Elapsed: 16251.024 s Mean Reward: 4.091. Std of Reward: 2.666. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 109000. Time Elapsed: 16398.547 s Mean Reward: 3.778. Std of Reward: 1.991. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 110000. Time Elapsed: 16546.638 s Mean Reward: 3.781. Std of Reward: 2.480. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 111000. Time Elapsed: 16695.037 s Mean Reward: 3.781. Std of Reward: 2.003. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 112000. Time Elapsed: 16844.596 s Mean Reward: 4.099. Std of Reward: 2.061. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 113000. Time Elapsed: 16993.850 s Mean Reward: 3.947. Std of Reward: 2.209. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 114000. Time Elapsed: 17141.868 s Mean Reward: 4.339. Std of Reward: 2.273. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 115000. Time Elapsed: 17289.755 s Mean Reward: 4.235. Std of Reward: 2.039. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 116000. Time Elapsed: 17437.739 s Mean Reward: 4.149. Std of Reward: 1.878. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 117000. Time Elapsed: 17584.437 s Mean Reward: 3.681. Std of Reward: 2.435. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 118000. Time Elapsed: 17731.656 s Mean Reward: 4.254. Std of Reward: 2.393. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 119000. Time Elapsed: 17878.347 s Mean Reward: 3.880. Std of Reward: 2.333. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 120000. Time Elapsed: 18032.821 s Mean Reward: 3.946. Std of Reward: 2.102. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 121000. Time Elapsed: 18182.555 s Mean Reward: 4.360. Std of Reward: 2.060. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 122000. Time Elapsed: 18329.819 s Mean Reward: 4.615. Std of Reward: 2.184. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 123000. Time Elapsed: 18476.947 s Mean Reward: 4.439. Std of Reward: 2.488. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 124000. Time Elapsed: 18625.525 s Mean Reward: 4.340. Std of Reward: 2.346. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 125000. Time Elapsed: 18773.509 s Mean Reward: 5.024. Std of Reward: 2.076. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 126000. Time Elapsed: 18920.294 s Mean Reward: 4.570. Std of Reward: 2.455. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 127000. Time Elapsed: 19069.109 s Mean Reward: 4.846. Std of Reward: 2.127. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 128000. Time Elapsed: 19215.364 s Mean Reward: 4.121. Std of Reward: 2.840. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 129000. Time Elapsed: 19362.128 s Mean Reward: 5.200. Std of Reward: 2.333. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 130000. Time Elapsed: 19507.516 s Mean Reward: 4.679. Std of Reward: 2.397. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 131000. Time Elapsed: 19654.820 s Mean Reward: 4.423. Std of Reward: 2.129. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 132000. Time Elapsed: 19800.818 s Mean Reward: 5.157. Std of Reward: 2.571. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 133000. Time Elapsed: 19948.526 s Mean Reward: 5.315. Std of Reward: 2.175. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 134000. Time Elapsed: 20093.952 s Mean Reward: 5.316. Std of Reward: 2.361. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 135000. Time Elapsed: 20241.100 s Mean Reward: 4.751. Std of Reward: 2.470. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 136000. Time Elapsed: 20388.281 s Mean Reward: 5.093. Std of Reward: 2.341. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 137000. Time Elapsed: 20534.602 s Mean Reward: 5.072. Std of Reward: 2.839. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 138000. Time Elapsed: 20680.579 s Mean Reward: 5.266. Std of Reward: 2.452. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 139000. Time Elapsed: 20828.518 s Mean Reward: 5.567. Std of Reward: 2.605. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 140000. Time Elapsed: 20975.996 s Mean Reward: 4.808. Std of Reward: 2.590. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 141000. Time Elapsed: 21121.415 s Mean Reward: 5.013. Std of Reward: 2.501. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 142000. Time Elapsed: 21269.006 s Mean Reward: 4.404. Std of Reward: 2.504. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 143000. Time Elapsed: 21416.877 s Mean Reward: 4.825. Std of Reward: 2.483. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 144000. Time Elapsed: 21563.210 s Mean Reward: 5.143. Std of Reward: 2.644. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 145000. Time Elapsed: 21711.650 s Mean Reward: 5.271. Std of Reward: 1.937. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 146000. Time Elapsed: 21857.809 s Mean Reward: 5.455. Std of Reward: 2.311. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 147000. Time Elapsed: 22003.061 s Mean Reward: 5.739. Std of Reward: 2.922. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 148000. Time Elapsed: 22150.563 s Mean Reward: 5.241. Std of Reward: 2.422. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 149000. Time Elapsed: 22297.132 s Mean Reward: 5.570. Std of Reward: 2.042. Training.
INFO:mlagents.envs:Saved Model
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 150000. Time Elapsed: 22443.141 s Mean Reward: 5.601. Std of Reward: 2.177. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 151000. Time Elapsed: 22588.277 s Mean Reward: 5.365. Std of Reward: 2.344. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 152000. Time Elapsed: 22733.502 s Mean Reward: 5.452. Std of Reward: 2.559. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 153000. Time Elapsed: 22879.225 s Mean Reward: 5.306. Std of Reward: 2.743. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 154000. Time Elapsed: 23026.272 s Mean Reward: 5.689. Std of Reward: 2.460. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 155000. Time Elapsed: 23172.627 s Mean Reward: 6.107. Std of Reward: 2.242. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 156000. Time Elapsed: 23320.439 s Mean Reward: 5.731. Std of Reward: 2.458. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 157000. Time Elapsed: 23466.249 s Mean Reward: 6.570. Std of Reward: 2.590. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 158000. Time Elapsed: 23614.418 s Mean Reward: 6.380. Std of Reward: 2.531. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 159000. Time Elapsed: 23761.627 s Mean Reward: 6.487. Std of Reward: 2.458. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 160000. Time Elapsed: 23957.094 s Mean Reward: 6.150. Std of Reward: 2.166. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 161000. Time Elapsed: 24106.028 s Mean Reward: 6.270. Std of Reward: 2.512. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 162000. Time Elapsed: 24254.963 s Mean Reward: 6.209. Std of Reward: 2.126. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 163000. Time Elapsed: 24403.525 s Mean Reward: 6.028. Std of Reward: 2.272. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 164000. Time Elapsed: 24551.706 s Mean Reward: 5.607. Std of Reward: 2.883. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 165000. Time Elapsed: 24700.496 s Mean Reward: 5.904. Std of Reward: 2.271. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 166000. Time Elapsed: 24850.272 s Mean Reward: 6.007. Std of Reward: 2.542. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 167000. Time Elapsed: 24998.971 s Mean Reward: 6.223. Std of Reward: 2.594. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 168000. Time Elapsed: 25149.023 s Mean Reward: 6.078. Std of Reward: 2.206. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 169000. Time Elapsed: 25297.894 s Mean Reward: 6.187. Std of Reward: 2.020. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 170000. Time Elapsed: 25446.918 s Mean Reward: 6.404. Std of Reward: 2.300. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 171000. Time Elapsed: 25594.592 s Mean Reward: 6.344. Std of Reward: 1.966. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 172000. Time Elapsed: 25743.850 s Mean Reward: 6.197. Std of Reward: 2.416. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 173000. Time Elapsed: 25892.364 s Mean Reward: 6.312. Std of Reward: 2.823. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 174000. Time Elapsed: 26041.911 s Mean Reward: 6.560. Std of Reward: 2.675. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 175000. Time Elapsed: 26193.324 s Mean Reward: 6.343. Std of Reward: 2.721. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 176000. Time Elapsed: 26343.375 s Mean Reward: 6.235. Std of Reward: 2.244. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 177000. Time Elapsed: 26490.571 s Mean Reward: 6.965. Std of Reward: 2.419. Training.
INFO:mlagents.trainers: firstRun-0: BouncerLearning: Step: 178000. Time Elapsed: 26638.531 s Mean Reward: 6.450. Std of Reward: 1.921. Training.
