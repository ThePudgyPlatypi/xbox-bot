# xbox-bot
A simple best buy bot to hopefully get an xbox

Download Zip https://github.com/ThePudgyPlatypi/xbox-bot/archive/refs/heads/main.zip with code and extract to a folder. 
Open CLI by going to search bar -> type ‘cmd’ (no quotes) and hit enter. In the new CLI that pops up type ‘python’ -> this will send you to the Microsoft store where you will download and install python. This is the easiest way to do it that I have found.
After python has downloaded and installed type ‘python’ into the CLI and you should see something like: 

You will need to install some dependencies for the script so hit Ctrl+Z then ENTER to exit the python command shell and type:
pip install -U selenium

Selenium is a python tool that enables all the webscraping. 

pip install chromedriver-autoinstaller

Chromedriver is what allows you to automate using Google Chrome

pip install twilio

Twilio is a REST API for automate SMS messaging among other things. 
Now you will need to setup a Twilio account so that you can have a message sent to your phone when the xbox or ps5 is in your cart and ready for checkout. You will have to do the final piece of the puzzle and finish checkout so act fast.
Go to twilio.com and sign up. This is a paid service but they give you 15 bucks free which should cover you since it only sends out a text when you actually have one in your checkout and twilio charges by the request and that would only count as one request. Basically you will be fine. Sign up for an account, and verify your email and phone. Once you verify your phone it will bring up a screen to start a project. Copy these settings: 
After hitting ‘Get Started with Twilio’ you will be taken to your dashboard where the only thing you care about is this: 
 
While in your dashboard signup for a twilio number. You get one with your trial account. There is nothing special about this step, just a couple clicks and you’re given a number.
Now open up xbox_bot in a text editor like NOTEPAD and enter in the twilio_cid, twilio_token, twilio_number, and phone_number (which is the number you want the reminder send to). Also your best buy account username and password
 
Go back to your CLI window and navigate to the director that you put the xbox_bot.py file in. You can change the drive by typing {driver_letter}: so “d:” to get to the D drive (no quotes) then to change directories use “cd” and the path to the file. For example my python file is in D:\Sites\Bot so I would type “d:” then enter then type “cd Sites\Bot” and hit enter. Also you can type some of the name the press TAB for it to autocomplete. 
Once in the root folder where you are keeping xbox_bot.py type “python xbox_bot.py” and it will run the script. If everything went well it will launch an instance of chrome and continuously try to see if the sold out button has been turned to add to cart. When it has it will click the add to cart, click go to cart and then send you a text message to finish the checkout. The message has a link to bestbuy cart checkout so make sure you signed into your best buy account on your phone to increase the speed of checkout and enter all the shipping info in your account to make it all quicker. Also, make sure that you don’t have something like two factor on your best buy account. Lastly, I wouldn’t run this 24/7 but instead use those twitter things and such that tell you roughly when a xbox might drop and start it that day. Would be best if your available to reset it. You may also want to setup multiple accounts in case you get locked out for a couple hours because of to many add to cart clicks. This can happen, and I have an exception for it, but it will wait two hours or so before it tries to add to cart again. An extra account running with this script in parallel can help
