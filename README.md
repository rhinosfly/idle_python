# idle_python v0.5.1

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
- moved submodules to submodules/
- added submodules/__init__.py
- removed file structure from README.md
