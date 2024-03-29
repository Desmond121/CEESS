# <img src="https://raw.githubusercontent.com/Desmond121/CEESS/aae96153555f5511812f78cb88c6ac9baf722a44/resources/img/icon.svg" width="30" height="30"> CEESS
A Chemical Engineering Experiments Safety Simulator, which provides 2 client apps for both teachers and students to enhance the process of chemical engineering safety education.

<p float="left">
  <img src="https://github.com/Desmond121/CEESS/blob/main/resources/img/screenshot/loginWindow.png" height="200" />
  <img src="https://github.com/Desmond121/CEESS/blob/main/resources/img/screenshot/autoclave.png" height="200" /> 
  <img src="https://github.com/Desmond121/CEESS/blob/main/resources/img/screenshot/grade.png" height="200" />
</p>

## Dependency:
- [Python 3.9.x](https://www.python.org/downloads/) or higher
- [Pyside2 5.15.x](https://pypi.org/project/PySide2/)
- [xlrd 2.x](https://pypi.org/project/xlrd/)
- [PyMySql](https://pypi.org/project/PyMySQL/)

To install all required python packages:
```
pip install pyside2 xlrd pymysql
```
## Build Instruction
You need [Pyinstaller](https://pypi.org/project/pyinstaller/) to build the execuable.

To avoid building a large executable file with redundant packages, you should create a python virtual environment in project directory first:
```
python -m venv ./virtualenvs
```
Then activate the virtual evironment:
- On windows:
```
./.virtualenvs/bin/activate.ps1
```
- On Linux:
```
source ./.virtualenvs/bin/activate
```
Once successfully enter the virtual environment, install all dependencies:
```
pip install PySide2 PyMySQL xlrd pyinstaller
```
Then build the executable with `Pyinstaller`:
```
pyinstaller -Fw ./run.py
```
Finally, copy the `run.exe` from directory `./dist/` to the root directory of this project. Then you can delete all files and folders in the project except:
- `./data/`. This is where the SQLite database file is located, you can delete it when you use MySQL.
- `./resources/`. This is where the fonts, icons or other resources are located.

## Database
CEESS support both SQLite and MySQL:
- SQLite. The data are not sharing between different clients. Student should use export module from student client to export their data and send to their teacher. Teachers can batch import those data into their local client. This is a super weird requirement by my tutor.😅
- MySQL. A more reasonable version.

To switch the version of client:

1. Navigate to ./utility/DataManager.py
2. Change the `_SQLITE` and `_MYSQL` flags following the comments.

To initialise the database:

*\*still in progress\**
