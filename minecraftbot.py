# BUILDS ONE BUILDING
currentBlock = "smooth_stone" # material type

# coordinates to fill entire section with block (not hollow)
y = 65
x = initialX
z = initialZ
coord += "{} {} {} ".format(x, y, z)
x += 14
y = 150
z -= 14
coord += "{} {} {}\n".format(x, y, z)

# writes fill command to fill section with block
for word in coord.splitlines():
    sleep(1)
    pyautogui.write("/")
    sleep(1)
    pyautogui.write("fill " + word + " " + currentBlock)
    pyautogui.press("enter")

# coordinates to hollow out building
aired = """"""

y = 65
x = initialX + 1
z = initialZ - 1
aired += "{} {} {} ".format(x, y, z)
x += 12
z -= 12
y = 149
aired += "{} {} {}\n".format(x, y, z)

# writes fill command to air out building
for word in aired.splitlines():
    sleep(1)
    pyautogui.write("/")
    sleep(1)
    pyautogui.write("fill " + word + " air")
    pyautogui.press("enter")

# builds the floors for each floor in the building
floor = """"""
y = 66 + 8
while (y < 150):
    x = initialX + 1
    z = initialZ - 1
    floor += "{} {} {} ".format(x, y, z)
    x += 12
    z -= 12
    floor += "{} {} {}\n".format(x, y, z)
    for word in floor.splitlines():
        sleep(1)
        pyautogui.write("/")
        sleep(1)
        pyautogui.write("fill " + word + " " + currentBlock)
        pyautogui.press("enter")
    floor = """"""
    y += 8

y = 66 + 7
while (y <= 150):
    x = initialX + 1
    z = initialZ - 1
    floor += "{} {} {} ".format(x, y, z)
    x += 12
    z -= 12
    floor += "{} {} {}\n".format(x, y, z)
    for word in floor.splitlines():
        sleep(1)
        pyautogui.write("/")
        sleep(1)
        pyautogui.write("fill " + word + " glowstone")
        pyautogui.press("enter")
    floor = """    """
    y += 8

z = initialZ-2
y = 68

# builds windows on each of the 4 sides of building
# side 1
while (z-3 > initialZ-15):
    window = """"""
    y = 68
    while (y < 150):
        x = initialX
        window += "{} {} {} ".format(x, y, z)
        z -= 2
        window += "{} {} {}\n".format(x, y, z)
        for word in window.splitlines():
            sleep(1)
            pyautogui.write("/")
            sleep(1)
            pyautogui.write("fill " + word + " glass")
            pyautogui.press("enter")
        window = """"""
        z += 2
        y += 8
    z -= 4

# side 2
x = initialX+2
while (x+3 < initialX+15):
    window = """"""
    y = 68
    while (y < 150):
        z = initialZ
        window += "{} {} {} ".format(x, y, z)
        x += 2
       #  y += 1
        window += "{} {} {}\n".format(x, y, z)
        for word in window.splitlines():
            sleep(1)
            pyautogui.write("/")
            sleep(1)
            pyautogui.write("fill " + word + " glass")
            pyautogui.press("enter")
        window = """"""
        x -= 2
        y += 8
    x += 4

# side 3
x = initialX+2
while (x+3 < initialX+15):
    window = """"""
    y = 68
    while (y < 150):
        z = initialZ - 14
        window += "{} {} {} ".format(x, y, z)
        x += 2
        window += "{} {} {}\n".format(x, y, z)
        for word in window.splitlines():
            sleep(1)
            pyautogui.write("/")
            sleep(1)
            pyautogui.write("fill " + word + " glass")
            pyautogui.press("enter")
        window = """"""
        x -= 2
        y += 8
    x += 4

# side 4
z = initialZ-2
while (z-3 > initialZ-15):
    window = """"""
    y = 68
    while (y < 150):
        # z = initialZ - 2
        x = initialX + 14
        window += "{} {} {} ".format(x, y, z)
        z -= 2
       #  y += 1
        window += "{} {} {}\n".format(x, y, z)
        for word in window.splitlines():
            sleep(1)
            pyautogui.write("/")
            sleep(1)
            pyautogui.write("fill " + word + " glass")
            pyautogui.press("enter")
        window = """"""
        z += 2
        y += 8
    z -= 4
x = 540
