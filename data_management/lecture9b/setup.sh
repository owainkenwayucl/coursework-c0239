#!/bin/bash

# This script build an environment for the examples in lecture 9b.
# It should be sourced so it affects the current shell

virtualenv wk9b
source wk9b/bin/activate
wd=$(pwd)
cd ../lecture9a/full_model
pip install -r requirements.txt
export PYTHONPATH=$(pwd):$PYTHONPATH
cd ${wd}
unset wd