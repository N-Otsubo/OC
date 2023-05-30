import pyautogui as pag
from time import sleep

# 指定の座標までマウスを動かす
# duration : 移動時間(s)
# pag.moveTo(500, 600, duration=3)

# カーソルの位置から移動
# pag.move(0, -200, duration=2)

# 文字の入力
# pyautogui.write("enter", interval=0.5)

pag.keyDown("command")
pag.press("space")
pag.keyUp("command")

pag.write("memo")

pag.press("enter")

sleep(1)

pag.keyDown("command")
pag.press("q")
pag.keyUp("command")
