MonitorCost = (int(input("Введите стоимость монитора: ")))
SysBlockCost = (int(input("Введите стоимость системного блока: ")))
KeyBoardCost = (int(input("Введите стоимость клавивтуры: ")))
MouseCost = (int(input("Введите стоимость мыши: ")))
Price = MouseCost + SysBlockCost + KeyBoardCost + MonitorCost
print ("Стоимость 3 компьютеров из этих комплектующих ", 3*Price, "₽")

n = (int(input("Введите необходимое количество компьютеров: ")))
print ("Стоимость ", n, " компьютеров из этих комплектующих ", n*Price, "₽")