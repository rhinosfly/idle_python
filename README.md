# idle_python v0.4

constantly in-progress idle game using pyray (raylib bindings for python) for Python practice

## directions
- install python
- install pyray
    - probably: `pip install python`
    - or: pip3 install python
- clone repository, or download files
- change to new directory
    - probably: `idle_python-main` if downloaded
    - `idle_python` if cloned
- run: `idle_python.py`
- or `python idle_python.py`

## features
- v0.1: click box -> increment money!
- v0.2: upgrade clicks
- v0.3: buy clickers
- v0.4: (new!) upgrade clicker speed

## changes
- added click speed upgrade, refactored clicks.py into clickers.py 
- Clicker class now has subclasses controlling each different upgrade

## file structure
- idle_python.py
	- contains:
    		- the main script
    	- imports:
        	- pyray
        	- General_Data
        	- Button
        	- Clicker
- clickers.py
	- contains:
		- Clicker class definition
    			- including list of clickers
    	- imports:
       		- pyray
           	- Button
       		- General_Data
- buttons.py
	- contains:
    	- Button (class definition)
    		- including dictionary of buttons
    - imports:
        - pyray
        - General_Data
- general_datas.py
	- contains
		- all globally shared data
	- imports
		- pyray
