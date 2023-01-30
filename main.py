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

# print('Best match top left position: %s' % str(max_loc))
# print('Best match confidence: %s' % max_val)
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
        if ingame != None:
            print('you are now connected to the server, good luck killing some finns')
            #send messenger message
            
            break
        elif joinserver != None:
            pyautogui.moveTo(joinserver)
            pyautogui.click(joinserver)
            print('Clicked join server')
        elif serverfull != None:
            pyautogui.moveTo(serverfull)
            pyautogui.click(serverfull)
            print('Server is full')

        else:
            print('Waiting for server to load')
            time.sleep(1)

        


        

            
            
            
            
        
            
            
            


            



    
         