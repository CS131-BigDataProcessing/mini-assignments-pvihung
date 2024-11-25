#!/bin/bash

python -m venv venv 

source venv/Scripts/activate

# khong su dung requirement.txt (do khong can den nhung cai nhu numpy, panda) 
# neu xai thi no se bi qua nen chi can xai pip va wheel la du
python -m pip install -U pip

python -m pip install -U wheel 

cd A11
python -m unittest discover -s . -p "unitTest_math_functions.py"

deactivate
