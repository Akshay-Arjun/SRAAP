# SRAAP
Exploitation of bugs in our college website.
SRAAP.py is used to download profile pictures,signatures,aadhar,pan of any student or faculty. </br>
You need to enter ROLLNUMBER to download picture of student and Employee Id to download picture of faculty.
# Installation & Usage:
### Python should be installed first ! Download it from here based on your operating system :
- Windows : https://www.microsoft.com/store/productId/9PJPW5LDXLZ5
- Linux : ``` sudo apt install python3 -y ```
- Android : Download Termux App from here https://f-droid.org/repo/com.termux_118.apk and install it. </br> Now Run : </br> ```termux-setup-storage``` </br>```apt update -y ``` </br> ```apt install git -y``` </br> ```apt install python3 -y```
## Linux & Android :
#### Installation 
```
git clone https://github.com/Akshay-Arjun/SRAAP
```
#### Usage
▶ Navigate to the SRAAP folder.
```
cd SRAAP
````
▶ Install requirements. (Only on 1st time usage)
```
pip install -r requirements.txt 
```
▶ Run the script.
```
python3 SRAAP.py
```
## Windows:
#### Installation 
- Download : https://github.com/Akshay-Arjun/SRAAP/archive/refs/heads/main.zip
- Extract the zip file.
#### Usage
- Open the extracted folder in File Explorer.
- Type ```cmd``` before the folder name to open command prompt in the extracted folder.
- ![ss](https://user-images.githubusercontent.com/68991993/156881801-c9c8f942-2d79-4a97-98df-e93a67f22618.png)
- ```pip install -r requirements.txt``` (Only on 1st time usage)</br>
- ``` python3 SRAAP.py ```
# Screenshots:
#### Android 

# Note:
Can get best results when used with Terminal because of some functions like 
``` 
installDir = os.path.dirname(os.path.abspath(__file__)) + '/' 
``` 
doesn't work in Notebooks like jupyter.
