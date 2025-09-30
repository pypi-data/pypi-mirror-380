#!/usr/bin/env bash


# 安装labkit到当前的python环境中

# 安装所有依赖
pip install -r requirements.txt

# 安装labkit
python setup.py install



# echo "export PYTHONPATH=$(pwd):\$PYTHONPATH" >>~/.bashrc
# echo "export PYTHONPATH=$(pwd)/../general:\$PYTHONPATH" >>~/.bashrc
# echo "export PATH=$(pwd)/bin:\$PATH" >>~/.bashrc
# # python setup.py install
# #pip install -r requirements.txt
# #pip install labkit
#
#
# # 设置virtualenv
