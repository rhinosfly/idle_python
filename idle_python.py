#!/usr/bin/python
#working progress idle game in pyray

import pyray as pr
from submodules import start_finish
from submodules.general_datas import General_Data
from submodules.buttons import Button 
from submodules.clickers import Clicker

start_finish.start()

while not pr.window_should_close():

    for name in Button.Dict:
        Button.Dict[name].onClick()
    for clicker in Clicker.Clickers.List:
        clicker.updateSelf()
        
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    for name in Button.Dict:
        Button.Dict[name].draw()
    for clicker in Clicker.Clickers.List:
        clicker.draw()
    pr.draw_text(f"{General_Data.money:,}", 10, 10, 20, pr.WHITE)
    pr.draw_text(f"click damage: {Clicker.Damage.value:,}", 10, 30, 20, pr.WHITE)
    pr.draw_text(f"clickers: {len(Clicker.Clickers.List):,}", 10, 50, 20, pr.WHITE)
    pr.draw_text(f"cps: {Clicker.Speed.clicks_per_second:,}",10,70,20,pr.WHITE)
    pr.draw_text(f"dps: {Clicker.Clickers.listLength*Clicker.Damage.value*Clicker.Speed.clicks_per_second:,}", 10,90, 20, pr.WHITE)

    pr.end_drawing()

start_finish.finish()
