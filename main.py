import cv2 as cv 
import numpy as np
import pyautogui 
import time

# Setup of images to be used
mainmenu = cv.imread('mainmenu.jpg', cv.IMREAD_UNCHANGED)
enlist = cv.imread('enlist.jpg', cv.IMREAD_UNCHANGED)
serverlist = cv.imread('serverlist.jpg', cv.IMREAD_UNCHANGED)
searchbox = cv.imread('searchbox.png', cv.IMREAD_UNCHANGED)
joinserver = cv.imread('joinserver.jpg', cv.IMREAD_UNCHANGED)
serverfull = cv.imread('serverfull.png', cv.IMREAD_UNCHANGED)


result = cv.matchTemplate(mainmenu, enlist, cv.TM_CCOEFF_NORMED)

# Get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# Prompt for server name
server_name = pyautogui.prompt(text='', title='Server Name or IP:PORT', default='135.181.165.173:8982')
if server_name is None:
    print('No server name entered. Exiting...')
    exit()
else:
    print('Server name entered: %s' % server_name)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found a match!')
    
    top_left = max_loc
    bottom_right = (top_left[0] + enlist.shape[1], top_left[1] + enlist.shape[0])
    
    # cv.rectangle(mainmenu, top_left, bottom_right,
    #              color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    
    # cv.imshow('Detected', mainmenu)
    #cv.waitKey(0)
    pyautogui.click(top_left)
    print('Clicked enlist button')
    
    # Wait for server list to load
    time.sleep(1)
    
    # Get server list search box coordinates
    x, y = pyautogui.locateCenterOnScreen('searchbox.png', confidence=0.8)
    print('Search box coordinates: %s, %s' % (x, y))
    
    # Click on search box
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()
    
    # Type server name from prompt
    pyautogui.typewrite(server_name)
    pyautogui.press('enter')
    print("Server name/ip entered:")
    print(server_name)
    
    # Wait for server to load
    time.sleep(5)
    
    while True:
        # Join server button click
        x, y = pyautogui.locateCenterOnScreen('joinserver.jpg', confidence=0.8)
            
        # Click on search box
        pyautogui.moveTo(x, y, 1)
        pyautogui.click()
                # Wait for server to load
        time.sleep(1)
        
        # Check if server is full
        if pyautogui.locateOnScreen('serverfull.png', confidence=0.8) is not None:
            print('Server is full. Trying again...')
            pyautogui.press('esc')
            
        else:
            print('Successfully joined server!')
            



    
         