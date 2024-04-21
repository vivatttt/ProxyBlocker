<p align="center">
      <img src="https://i.ibb.co/dtzf9ch/image.png" width="500">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/mitmproxy-10.3.0-purple">
   <img src="https://img.shields.io/badge/Flask-3.0.3-green">
</p>

## About
This system is designed to restrict access to unnecessary or harmful websites<br>
There are potentially two scenarios in which ProxyBlocker can be useful 
1. **If it is necessary to restrict the child's access to harmful resources**
2. **If you want to focus on something and limit yourself from the temptation to be distracted by social networks, streaming platforms, etc**

## Getting started
To launch the **ProxyBlocker** download the repository folder and run following on your **Linux** PC

Download the Virtual Enviroment
```shell
python3 -m venv env
```
```shell
source env/bin/activate
```
Install all the necessary frameworks
```shell
pip install -r requirements.txt
```
Install and configure .env
```shell
touch .env
```
Сome up with and fill in the username and password under which you will enter the admin panel in .env
```.env
ADMIN_LOGIN=
PASSWORD_LOGING=
```
Then you need to configure PROXY in your prowser<br>
Run following to generate the certificate
```shell
mitmproxy
```
And go to `~/.mitmproxy/`. Find `mitmproxy-ca-cert.pem` and add it to your browser proxy-certificates.<br>
[Read more](https://docs.mitmproxy.org/stable/concepts-certificates/)

<br>
And we're done with configuration

## User Manual <br>

Open two terminals - in one we will launch a proxy server, in the other a processing server<br>
Go to main directory in first terminal and run
```shell
make run_proxy
```
Go to main directory in second terminal and run
```shell
make run_flask
```
To block / unblock sites go to `localhost:8000/admin`<br>
Add login information as `password=`, `login=`<br>
The overall url is
```url
https://localhost:8000/admin?login=<your_login>&password=<your_password>
```
And you will see the admin panel
<p align="center">
      <img src="https://i.ibb.co/J36p666/image.png" width="1200">
</p>
To add or delete new site (sites) fill the form with it's domain name and method (add or delete)<br>

For example you want to block `tiktok.com`. Submit:
<p align="left">
      <img src="https://i.ibb.co/MpXkxJ2/image.png" width="700">
</p>
The domain name has been added to the blocked list
<p align="left">
      <img src="https://i.ibb.co/YhjBmtc/image.png" width="700">
</p>

And now instead of this
<p align="left">
      <img src="https://i.ibb.co/rZ3H7vr/image.png" width="1200">
</p>

**You get this and a bunch of motivation to get better and develop not waste your time**

<p align="left">
      <img src="https://i.ibb.co/ZNSLKMZ/image.png" width="1200">
</p>
<br>
<br>

### Important remark

**Some browsers put blocked sites in the cache and it needs to be cleaned manually if you want to revive some site.**<br>
[Read more](https://its.uiowa.edu/support/article/719)

