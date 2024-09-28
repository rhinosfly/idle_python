# idle_python v0.5

constantly in-progress idle game using pyray (raylib bindings for python) for Python practice

## directions
- install python
- install pyray
    - probably: `pip install python`
    - or: pip3 install python
- clone repository, or download files
- change to new directory
- run: `idle_python.py`
- or:  `python idle_python.py`

## features
- v0.1: click box -> increment money!
- v0.2: upgrade clicks
- v0.3: buy clickers
- v0.4: upgrade clicker speed
- v0.5: (new!) save your progress

## changes
- added start_finish.py
- controls all init and closing, including read and write functions to "saveState.json. Calls each class' respective read and write functions.

## file structure
- idle_python.py
	- contains:
    		- the main script
    	- imports:
        	- pyray
        	- start_finish
        	- General_Data
        	- Button
        	- Clicker   	
- buttons.py
	- contains:
    	- Button (class definition) - including dictionary of buttons
    - imports:
        - pyray
- clickers.py
	- contains:
		- Clicker class definition
    			- including list of clickers
    	- imports:
       		- pyray
           	- Button
       		- General_Data
- general_datas.py
	- contains
		- all globally shared data
	- imports
		- pyray
- start_finish.py
	- contains:
		- initialize and uninitialize functions
		- read and write functions, calling each respective class's read and write methods