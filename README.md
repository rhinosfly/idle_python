# idle_python v0.2

constantly in-progress idle game using pyray (raylib bindings for python) for python practice

### directions
- install python
- install pyray
    - probably: `pip install pyray`
- clone repositry, or download files
- change to new directory
    - probably: `idle_python-main`
- run: `python idle_python.py`

### features
- click box -> increment money!
- upgrade clicks

### file structure
- idle_python.py
	- contains
    	- the main script
    - imports
        - pyray
        - buttons
        - data
- buttons.py
	- contains
    	- Button (class definition)
    	- List (of buttons)
    - imports
        - pyray
        - data
- data.py
	- contains
		- all dynamic data 
		- Click (class definition)
	- imports
		- pyray
