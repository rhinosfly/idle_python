#working progress idle game in pyray

import pyray as pr
import Button

def increment():
    global money
    money += clickValue

def upgradeClickValue():
    global clickValue, clickValueCost, money, buttons
    if money >= clickValueCost:
        money -= clickValueCost
        clickValueCost *= 2
        clickValue += 1
        buttons[1].name = str(clickValueCost) + ": click damage +1"

pr.init_window(800,400,"idle game")
pr.set_target_fps(60)

money = 0
clickValue = 1
clickValueCost = 20

buttons = [Button.Button(600,100,50,50,pr.RED,"click me",increment),
           Button.Button(20,100,50,20,pr.BLUE, str(clickValueCost) + ": click damage +1", upgradeClickValue)]



while not pr.window_should_close():
    #run all button functions if clicked
    for button in buttons:
        button.onClick()
        
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    for button in buttons:
        button.draw()
    pr.draw_text(f"{money}", 10, 10, 20, pr.WHITE)
    pr.draw_text("click damage: " + str(clickValue), 10, 30, 20, pr.WHITE)
    pr.end_drawing()

pr.close_window()
