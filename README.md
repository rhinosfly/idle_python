# idle_python v0.3.1

constantly in-progress idle game using pyray (raylib bindings for python) for Python practice

### directions
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

### features
- v0.1: click box -> increment money!
- v0.2: upgrade clicks
- v0.3: (new!) buy clickers

### file structure
- idle_python.py
	- contains:
    		- the main script
    	- imports:
        	- pyray
        	- General_Data
        	- Button
        	- Clicker
        	- Click
- clickers.py
	- contains:
		- Clicker class definition
    			- including list of clickers
    	- imports:
       		- pyray
           	- Button
       		- General_Data
- clicks.py
  	- contains:
  		- Click class definition
	- imports:
		- pyray
    		- General_Data
    		- Button
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
