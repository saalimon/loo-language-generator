# Loo-Language-Generator
Loo Language Generator
## Test Loo Language generator module
  Loo language module is in functions directory (function.py)
  you can test this module by using loomain(inputText) function 
### example 
  > from functions import loomain <br>
  > loomain("ไปกินข้าว")
### or you can test on
  > https://loolang.herokuapp.com/

## How to deploy flask local website
* python3 -m venv ~/.virtualenvs/loolang 
  * _for create virtual environment_
* source ~/.virtualenvs/loolang/bin/activate
* python -m pip install requirements.txt
  * _for install requirements python package module_
* python app.py 
  * _start flask app at port 5000
* deactivate

