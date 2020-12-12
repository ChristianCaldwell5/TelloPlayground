# TelloPlayground
A one stop shop for getting the Tello EDU flying through the command line, code, and custom commands. 

# TelloSDK 
This folder includes three important files: 
1. Tello SDK 2.0 User Guide.pdf - Provides native Tello commands that can be used at the command line. 
2. Tello Mission Pad User Guide.pdf - Provides instructions and commands for making the Tello interact with the mission pads. 
3. Tello3.py - The official Python3 control demo for Tello. A great place to start for beginners!

# Using Tello3.py
1. Turn on your Tello. 
2. Connect to the Tello via WiFi by selecting the Tello from your WiFi/Network settings. 
3. Navigate through your Terminal, GitBash, ect. to the **TelloSDK** folder.
4. Run `python3 Tello3.py`. 
5. You can now enter commands as seen in the guides provided within the same folder to get your Tello flying. 

# Using telloFlight.py 
telloFlight.py offers a better command line experience by including native and custom options for Tello flight outside of the SDK's. 
Custom commands can be added by altering the **telloFunctions.py** file and then calling those functions in **telloFlight.py** when input matches that command. 
1. Turn on your Tello. 
2. Connect to the Tello via WiFi by selecting the Tello from your WiFi/Network settings. 
3. Navigate through your Terminal, GitBash, ect. to the **Code** folder.
4. Run `python3 telloFlight.py`. 
5. You can now enter native **AND** custom commands you created (or use the custom ones created and displayed already).

# easyTello API
The **easyTello** folder included is an API for the Tello which helps with socket connection, command sending, response retrieval, and Tello objects for 
programming and running. 
This API is included for convenience, but is originally found [here](https://github.com/Virodroid/easyTello).   
Click [here](https://github.com/Virodroid/easyTello) for more details on the easyTello API.

# custom_easyTello
This folder is for customizing the easyTello API and altering it for more functionality or tweaks.    
Changes have been made to the **tello.py** file for momevement and control commands.  
  
To use the custom API, switch out the import found within **telloFlight.py**.  

Before: `from easyTello.easytello import tello`.  
After: `from custom_easyTello.easytello import tello`.  
