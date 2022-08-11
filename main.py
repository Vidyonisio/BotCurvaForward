import pyautogui
import time
import datetime

"curva na tela da esquerda opera com scroll no topo: Point(x=306, y=316)"
"Botão Consultar data: Point(x=548, y=315)"
"Botão Exportar p/ excel: Point(x=1262, y=352)"

d_mes = int(input('Quantos dias tem o mês? '))
date_entry = input('Coloque a Data inicial no formato: DD/MM/YYYY: ')
day1, month, year = map(int, date_entry.split('/'))
#date = datetime.date(year, month, day)
day = day1

def str_lista(d,m,y):
    if month < 10:
        if day < 10:
            lista = ["0"+str(day),"0"+str(month),str(year)]
        else:
            lista = [str(day), "0" + str(month), str(year)]
    else:
        if day < 10:
            lista = ["0"+str(day),str(month),str(year)]
        else:
            lista = [str(day), str(month), str(year)]

    string_lista = '/'.join(lista)
    return (string_lista)

def bot(data):
    pyautogui.moveTo(306,316)
    pyautogui.click()
    pyautogui.doubleClick()
    time.sleep(0.1)
    pyautogui.typewrite(data)
    time.sleep(0.1)
    pyautogui.click(548,315)
    time.sleep(1.2)  #1.2
    pyautogui.moveTo(1262,352)
    time.sleep(0.08)
    pyautogui.click()

for i in range(d_mes-day1+1):
    data_str=str_lista(day, month, year)
    print(data_str)
    bot(data_str)
    day +=1
    time.sleep(1.6) #1




print(day)
print(day1)