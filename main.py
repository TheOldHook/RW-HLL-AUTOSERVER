import pyautogui 
import time
import os

# Prompt for server name
server_name = pyautogui.prompt(text='', title='Server Name', default='Finns Let Loose')
time.sleep(1)
if server_name is None:
    print('No server name entered. Exiting...')
    exit()
else:
    print('Server name entered: %s' % server_name)


time.sleep(4)
searchbox = pyautogui.locateCenterOnScreen('searchbox.jpg', confidence=0.7)

if searchbox != None:
    print('Found a match!')
    time.sleep(1)
    pyautogui.moveTo(searchbox)
    pyautogui.click(searchbox)
    print('Clicked searchbox')
    
    time.sleep(1)
    # Type server name from prompt
    pyautogui.typewrite(server_name)
    pyautogui.press('enter')
    print("Server name entered: %s" % server_name)
    
    # Wait for server to load
    #time.sleep(1)
    

    # Click server
    while True:
        joinserver = pyautogui.locateCenterOnScreen('joinserver.jpg', confidence=0.7)
        serverfull = pyautogui.locateCenterOnScreen('ok.jpg', confidence=0.9)
        ingame = pyautogui.locateCenterOnScreen('ingame.jpg', confidence=0.7)
        if ingame != None: # If you are already in game, exit the script
            print('you are now connected to the server, good luck killing some finns')       
            break
        elif joinserver != None: # Try connecting to the server
            pyautogui.moveTo(joinserver)
            pyautogui.click(joinserver)
            print('Clicked join server')
        elif serverfull != None: # If the server is full, reconnect
            pyautogui.moveTo(serverfull)
            pyautogui.click(serverfull)
            print('Server is full')
        else:
            time.sleep(2)
            print('Waiting for server to load')

        


        

            
            
            
            
        
            
            
            


            



    
         