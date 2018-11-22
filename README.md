# Evenicle-AutoGrinder
A bot that helps you to grind in the game Evenicle by Alicesoft. It uses the pyautogui library for the image recognition and the automation part and the psutil library to detect for the game process

# What the bot does
Once it detects that you are in the main campaign view, it moves the character around in a square to raise the caution meter to make an encounter appear.
When an encounter appears and you are in the fight sequence, the bot will then detect for the autobattle button and click on it to initiate autobattle
Once the victory screen appears, the bot will detect it and click to close it and move you back to the campaign view.
This will constantly repeat until the script is unable to detect the campaign view and also the autobattle button

# Some guidelines
If you want to stop the script the easiest is to press esc and open the game menu, this causes the script to pretty much stop and allows you to move your cursor again

If the script doesn't work anymore, usually restarting the game helps.

