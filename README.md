
#########################
############### Sabia ###
#########################

Sabia is a CLI for the 'Davinci-003' model from OpenAI.
The bot will tell stories, write code, answer questions,
give you recipes, tell you how to build a jet engine, etc.

STEP 1. # Sign Up

#################
## GET API KEY ##
#################

a. To begin you must sign up at 
https://platform.openai.com/account/api-keys 
b. Once you have signed in click the large black circle first letter of your name in the top right corner
c. Click API keys (retrieve or get API keys)
d. Open the config.yml file in the Sabia directory
e. Place your api key on the right of Apikey: 

MAKE SURE THERE IS A SPACE BETWEEN apiKey: AND YOUR API KEY OTHERWISE IT WILL NOT BE RECOGNIZED AND WILL NOT WORK!
apiKey: <apikeyhere>

STEP 2. # Installation

#################
#### LINUX ######
#################

git clone https://github.com/jbhntr861/Sabia
cd Sabia
sudo apt install python3
pip install -r requirements.txt
python3 Sabia

#################
#### WINDOWS ####
#################

a. Windows key + X
b. Open Powershell terminal (admin)
   Install-Package Python3
   Install-Package git
   git clone https://github.com/jbhntr861/Sabia
   cd Sabia
   pip install -r requirements.txt
   Python3 Sabia

Enjoy.
