# モジュールのインポート
import pyautogui
import pyperclip
from time import sleep

# アンケートを表示
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")

pyautogui.write("Google")

pyautogui.press("enter")

pyautogui.hotkey("command", "l")
pyperclip.copy("https://docs.google.com/forms/d/e/1FAIpQLSdSQz2bk98O0S-kW8b76sWEtxjaibA0m6qru7RVEJSPXmPBXw/viewform")
pyautogui.hotkey("command", "v")

pyautogui.press("enter")

sleep(1)

# 各項目に情報を入力
# ご氏名
for i in range(0, 3):
    pyautogui.press("tab")

sleep(0.5)
pyperclip.copy("大坪　直之")
pyautogui.hotkey("command", "v")

pyautogui.press("tab")
sleep(0.5)

print("氏名....OK!")

# 1. QRコード上部にあるブース番号を入力してください。
pyperclip.copy("999999")
pyautogui.hotkey("command", "v")

pyautogui.press("tab")
sleep(0.5)

print("1....OK!")

# 2. QRコード下部にある番号を選択してください。
pyautogui.press("space")
pyautogui.press("down")

pyautogui.press("tab")
sleep(0.5)

print("2....OK!")

# 3. この1時間は、参加してみて率直にいかがでしたか？当てはまるものを選択してください。
pyautogui.press("space")
for i in range(0, 9):
    pyautogui.press("tab")
    sleep(0.5)

print("3....OK!")

# 4. この仕事に対して興味が湧きましたか？
pyautogui.press("space")
pyautogui.press("tab")
sleep(0.5)

print("4....OK!")

# 5. 将来、この仕事をしている自分の姿をイメージできましたか？
pyautogui.press("space")
pyautogui.press("tab")
sleep(0.5)

print("5....OK!")

# 6. 今の気持ちに最も近いものを1つ選んでください。
pyautogui.press("space")
pyautogui.press("tab")
sleep(0.5)

print("6....OK!")

# 画面TOPからゆっくりとスクロールする
# 現在のマウスカーソル位置を取得
m_posi_x, m_posi_y = pyautogui.position()

# スクロール
pyautogui.scroll(2000, m_posi_x, m_posi_y)

for i in range(0, 35):
    sleep(0.2)
    pyautogui.press("down")

print("All OK! !!")
