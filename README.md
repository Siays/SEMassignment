python 10
run requirements.txt => pip install -r requirements.txt

use only personal email for firebase, tarumt email will be blocked.

rename your fb_admin_sdk_e.py to fb_admin_sdk.py

before this make sure accepted my invitation 
!!!!Creating private key!!!!
1. go to firebase console home page
2. on left the side bar click on the "gear icon"(project settings) > SEMassignment > go to service accounts > scroll down and generate new private key
   a json file will be downloaded automatically, move the json file to where you put your project,
3. and in the fb_admin_sdk.py, replace your private key
   cred = credentials.Certificate("yourPrivateKey.json")

remember to add yourPrivateKey.json (can be named whatever you want) to .gitignore

btw, my database tested only to store/retrieve images and videos, if you guys need any other usage may need to explore yourself.
