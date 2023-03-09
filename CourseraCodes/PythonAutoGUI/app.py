import pyautogui

#lista de todas as keys em: print(pyautogui.KEYBOARD_KEYS)

#pyautogui.write("texto")#pyautogui.write("texto") -> insere o texto que vc quiser em alguma coisa que aceite texto

#pyautogui.press('nome_da_key') -> pressiona uma tecla do teclado

#pyautogui.sleep(2) -> espera em segundos

#pyautogui.position() -> pega a posição do mouse na hora que esse comando rodar

#pyautogui.moveTo(x_pos, y_pos) -> move o cursor para essa posição

#pyautogui.click() -> clique esquerdo do mouse

#pyautogui.dragTo(x, y, duration_in_seconds) -> arrasta o mouse para o local indicado durante o tempo indicado

#pyautogui.locateOnScreen('image_of_what_u_want.png') -> localiza o que você quiser na tela e retorna uma Box() com informações

pyautogui.alert("Starting automation...")#texto de alerta, igual no JavaScript
pyautogui.PAUSE = 0.1  #A cada linha de código executada, o programa vai esperar esse tempo para executar a próxima

SLEEP_DELAY = 0.75
CONFIDENCE = 0.9

def Find(what, max_tries = 10):
    err = pyautogui.locateCenterOnScreen(what, confidence=CONFIDENCE)
    for z in range(max_tries):
        if err == None:#ImageNotFoundException:
            print('Searching for: '+ what)
            err = pyautogui.locateCenterOnScreen(what, confidence=CONFIDENCE)
            pyautogui.sleep(SLEEP_DELAY)
        else:
            break
    return err

def CertainlyFind(what):
    err = pyautogui.locateCenterOnScreen(what, confidence=CONFIDENCE)
    while err == None:#ImageNotFoundException:
        print('Searching for: '+ what)
        err = pyautogui.locateCenterOnScreen(what, confidence=CONFIDENCE)
        pyautogui.sleep(SLEEP_DELAY)
    return err

def DragClicked(from_x, from_y, to_x, to_y, duration):
    pyautogui.moveTo(from_x, from_y)
    pyautogui.mouseDown()
    pyautogui.dragTo(to_x, to_y, duration)
    pyautogui.mouseUp()





def Buy25Tickets(amount):
    pyautogui.click(Find('PythonAutoGUI/Images/CloseButton.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/GoToShop.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/GoToSupplies.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/GoToTickets.png'))
    for z in range(amount):
        pyautogui.click(CertainlyFind('PythonAutoGUI/Images/Buy25Tickets.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/CloseButton.png'))

def SetFight():
    pyautogui.click(Find('PythonAutoGUI/Images/CloseButton.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/GoToFightButton.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/GoToCampaign.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/OmegaDivision.png'))
    pyautogui.click(CertainlyFind('PythonAutoGUI/Images/GreaterCairo.png'))
    pyautogui.sleep(SLEEP_DELAY)
    pyautogui.moveTo((1010, 215))#(1010, 215)
    pyautogui.click()

def LoopFight(times = 5) -> None:
    for z in range(times):
        pyautogui.click(CertainlyFind('PythonAutoGUI/Images/FightButton.png'))
        #click at fight

        pyautogui.click(Find('PythonAutoGUI/Images/HealButton.png'))
        
        while Find('PythonAutoGUI/Images/Use10.png', 2) != None:
            pyautogui.click(Find('PythonAutoGUI/Images/Use10.png', 2))
            pyautogui.sleep(SLEEP_DELAY/2)

        pyautogui.moveTo((620, 368))#(620, 368)
        pyautogui.click()
        pyautogui.moveTo((620, 478))#(620, 478)
        pyautogui.click()
        pyautogui.moveTo((620, 599))#(620, 599)
        pyautogui.click()

        pyautogui.click(CertainlyFind('PythonAutoGUI/Images/FightButton.png'))
        #click at fight
        
        pyautogui.click(CertainlyFind('PythonAutoGUI/Images/NoTagButton.png'))
        #click at no tag

        pyautogui.click(CertainlyFind('PythonAutoGUI/Images/FightButton.png'))
        #click at fight

        for z in range(2):
            pyautogui.click(CertainlyFind('PythonAutoGUI/Images/TripleSabre.png'))
            #certainly wait untill see the button

            pyautogui.click(CertainlyFind('PythonAutoGUI/Images/Enemy1.png'))
            #certainly wait untill see the enemy1

            pyautogui.sleep(1)

        for z in range(2):
            pyautogui.click(CertainlyFind('PythonAutoGUI/Images/Enemy2.png'))
            #certainly wait untill see the enemy1
            pyautogui.moveTo((10, 10))
            pyautogui.sleep(4)
            
            pyautogui.click(CertainlyFind('PythonAutoGUI/Images/Enemy2.png'))
            #certainly wait untill see the enemy1
            pyautogui.moveTo((10, 10))
            pyautogui.sleep(1)
            
            pyautogui.click(CertainlyFind('PythonAutoGUI/Images/CrushingFistAttack.png'))
            #wait untill see the button

            pyautogui.click(CertainlyFind('PythonAutoGUI/Images/Enemy2.png'))
            #certainly wait untill see the enemy1
            pyautogui.moveTo((10, 10))
            pyautogui.sleep(4)

        pyautogui.click(CertainlyFind('PythonAutoGUI/Images/CloseButton.png'))

LoopFight(3)