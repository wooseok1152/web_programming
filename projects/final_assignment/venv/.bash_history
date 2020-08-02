sudo update-alternatives --install y
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
cd ..
ls
python test.py
python file_zilla_test.py
cd ~
clear
ls
python file_zilla_test.py 
python app.py
sudo apt-get update
sudo apt-get install -y python3-pip
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
pip --version
pip install flask
ls
clear
ls
python file_zilla_test.py 
python app.py 
exit
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
ls
my@ChoiLaptop MINGW64 /c
$ ls
'!!ABi'/                                Log/
'!$sPC'/                                pagefile.sys
'!$tNXIG'/                              PerfLogs/
'$GetCurrent'/                         'Program Files'/
'$Recycle.Bin'/                        'Program Files (x86)'/
'Documents and Settings'@               selog.txt
my@ChoiLaptop MINGW64 /c
$ ssh -i /c/Users/my/Downloads/sparta-newkey2.pem ubuntu@http://15.164.213.38
ssh: Could not resolve hostname http://15.164.213.38: Name or service not known
my@ChoiLaptop MINGW64 /c
$ ssh -i /c/Users/my/Downloads/sparta-newkey2.pem ubuntu@15.164.213.38
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-1065-aws x86_64)
73 packages can be updated.
38 updates are security updates.
Last login: Sat Jun 20 04:58:23 2020 from 125.128.55.104
ubuntu@ip-172-31-37-78:~$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
OK
ubuntu@ip-172-31-37-78:~$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
OK
ubuntu@ip-172-31-37-78:~$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse
ubuntu@ip-172-31-37-78:~$ sudo apt-get update
Hit:1 http://ap-northeast-2.ec2.archive.ubuntu.com/ubuntu bionic InRelease
Hit:2 http://ap-northeast-2.ec2.archive.ubuntu.com/ubuntu bionic-updates InRelease
Hit:3 http://ap-northeast-2.ec2.archive.ubuntu.com/ubuntu bionic-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu bionic-security InRelease
Ign:5 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 InRelease
Get:6 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 Release [3951 B]
Get:7 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 Release.gpg [801 B]
Get:8 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse arm64 Packages [6490 B]
Get:9 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 Packages [6761 B]
Fetched 18.0 kB in 2s (10.2 kB/s)
Reading package lists... Done
ubuntu@ip-172-31-37-78:~$ sudo apt-get install -y mongodb-org
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
The following NEW packages will be installed:
0 upgraded, 5 newly installed, 0 to remove and 68 not upgraded.
Need to get 97.7 MB of archives.
After this operation, 296 MB of additional disk space will be used.
Get:1 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-shell amd64 4.2.8 [12.1 MB]
Get:2 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-server amd64 4.2.8 [18.5 MB]
Get:3 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-mongos amd64 4.2.8 [10.2 MB]
Get:4 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-tools amd64 4.2.8 [57.0 MB]
Get:5 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org amd64 4.2.8 [3524 B]
Fetched 97.7 MB in 3s (33.7 MB/s)
Selecting previously unselected package mongodb-org-shell.
(Reading database ... 63193 files and directories currently installed.)
Preparing to unpack .../mongodb-org-shell_4.2.8_amd64.deb ...
Unpacking mongodb-org-shell (4.2.8) ...
Selecting previously unselected package mongodb-org-server.
Preparing to unpack .../mongodb-org-server_4.2.8_amd64.deb ...
Unpacking mongodb-org-server (4.2.8) ...
Selecting previously unselected package mongodb-org-mongos.
Preparing to unpack .../mongodb-org-mongos_4.2.8_amd64.deb ...
Unpacking mongodb-org-mongos (4.2.8) ...
Selecting previously unselected package mongodb-org-tools.
Preparing to unpack .../mongodb-org-tools_4.2.8_amd64.deb ...
Unpacking mongodb-org-tools (4.2.8) ...
Selecting previously unselected package mongodb-org.
Preparing to unpack .../mongodb-org_4.2.8_amd64.deb ...
Unpacking mongodb-org (4.2.8) ...
Setting up mongodb-org-shell (4.2.8) ...
Setting up mongodb-org-mongos (4.2.8) ...
Setting up mongodb-org-tools (4.2.8) ...
Setting up mongodb-org-server (4.2.8) ...
Adding system user `mongodb' (UID 111) ...
Adding new user `mongodb' (UID 111) with group `nogroup' ...
Not creating home directory `/home/mongodb'.
Adding group `mongodb' (GID 115) ...
Done.
Adding user `mongodb' to group `mongodb' ...
Adding user mongodb to group mongodb
Done.
Setting up mongodb-org (4.2.8) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
ubuntu@ip-172-31-37-78:~$
```bash
# 실행. 아무 반응이 없으면, 잘 실행된 것!
# 리눅스는 보통 잘 되면 아무것도 안나와요!^^;
sudo service mongod start
# 아래 명령어를 입력해서 127.0.0.1:27017 이 있는지 확인하기
# 있다면 mongoDB가 정상 작동 중이라는 뜻입니다.
netstat -tnlp
mongo
sudo service mongod restart
sudo vi /etc/mongod.conf
clear
sudo service mongod restart
netstat -tnlp
sudo service mongod restart
netstat -tnlp
sudo vi /etc/mongod.conf 
clear
sudo service mongod restart
netstat -tnlp
sudo service mongod restart
netstat -tnlp
mongo
sudo vi /etc/mongod.conf 
clear
sudo service mongod restart
netstat -tnlp
cd ..
ls
lcear
clear
ls
cd home
clear
ls
cd ~
clear
ls
cd ..
clear
ls
cd home
cd ..
cd root
cd ~
clear
ls
cd ..
ls
cd ubuntu/
celar
clear
ls
su
clear
ls
cd ..
ls
clear
su
ls
clear
su
clear
ls
cd ubuntu/
clear
ls
cd alonememo/
clear
ls
python app.py
clear
sudo whoami
clear
ls
pip install requests beautifulsoup4 pymongo
clear
python app.py
clear
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000
python app.py
nohup python app.py &
ps -ef | grep 'python'
nohup python app.py &
exit
clear
ls
ps
clear
ps
exit
clear
ps
clear
ls

ps -ef | grep 'python'
tmp
ps -ef
exit
