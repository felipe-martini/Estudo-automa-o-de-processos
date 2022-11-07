import time

import pyautogui

pyautogui.alert(
    "O processo será iniciado, por gentileza não mexer no mouse nem no teclado durante o processo.")
pyautogui.PAUSE = 0.5

# abrir o google drive no meu computador

pyautogui.press("winleft")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://drive.google.com/drive/u/0/my-drive")
time.sleep(2)
pyautogui.press("enter")

# entrar na area de trabalho
time.sleep(3)
pyautogui.hotkey("winleft", "d")

# clicar no arquivo
time.sleep(1)
pyautogui.moveTo(1315, 33)
pyautogui.mouseDown()
# arrastar até a aba do opera que está aberta
pyautogui.moveTo(651, 718)
pyautogui.hotkey("altleft", "tab")

# soltar o arquivo dentro do drive
time.sleep(4)
pyautogui.mouseUp()


# esperar 5 segundos
time.sleep(5)
pyautogui.alert("Backup finalizado meu querido, pra cima deles")
