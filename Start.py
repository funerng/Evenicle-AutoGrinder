import pyautogui as auto
import psutil as psu
from time import sleep

# This is a grinding bot created for the game Evenicle, an eroge created by Alicesoft
# All it does is move around the map to raise the caution meter until a fight appears
# If a fight appears, the bot will click on autobattle button to have the game autobattle
# And when a victory screen appears it will click so that it closes and moves you back to the map view
# This bot works best if you have Gurigura on your team so the instant battle end appears which saves time
# If the bot happens to break, a quick restart on the game should fix it
# This script uses the pyautogui library for the automation and image recognition and the psutil library for game detection
# Script created by funerng


# The game automation
def mob_farm():

    # Constantly checks whether or not you are at campaign view
    var = -1
    x=0
    y=0
    while var < 0:
        is_at_field_screen = auto.locateOnScreen('FieldMenu.png', grayscale=True)
        print(is_at_field_screen)
        sleep(1)
        if is_at_field_screen is not None:
            print("campaign screen detected")
            x = is_at_field_screen[0]
            y = is_at_field_screen[1]
            auto.moveTo(x + 530, y + 350)
            while is_at_field_screen == auto.locateOnScreen('FieldMenu.png'):
                delay = 0.5
                auto.dragRel(60, 0, delay, auto.easeInOutQuad, button='left', )
                auto.dragRel(0, 100, delay, auto.easeInOutQuad, button='left')
                auto.dragRel(-60, 0, delay, auto.easeInOutQuad, button='left')
                auto.dragRel(0, -100, delay, auto.easeInOutQuad, button='left')


        else:
            print("campaign map not found / in battle")
            # checks if in combat
            in_combat = auto.pixelMatchesColor(x, y + 700, (160, 182, 191))
            auto_battle_btn_x, auto_battle_btn_y = (x, y + 700)
            if in_combat is True:
                print("In battle detected")
                auto.moveTo(auto_battle_btn_x, auto_battle_btn_y)
                auto.click(clicks=1)
                print("auto battle activated")
                while in_combat is True:
                    vic = auto.pixelMatchesColor(x + 748, y + 69,
                                                 (227, 201, 138))
                    if vic is True:
                        print("click")
                        auto.click(clicks=3, interval=0.2)
                        in_combat = False




# Game Detection
game_name = 'Evenicle.exe'
game_running = False
# Constant loops that checks whether or not the game is running
while not game_running:
    for p in psu.process_iter(attrs=['name']):
        if p.info['name'] == game_name:
            game_running = True
            break
    # Prompts user whether or not to start the script
    if game_running is True:
        print("game is running")
        start = input("Do you want to start farming? Y/N")
        if start == "Y":
            mob_farm()
    else:
        print("game is not running retrying in 2 seconds")
    sleep(1)
