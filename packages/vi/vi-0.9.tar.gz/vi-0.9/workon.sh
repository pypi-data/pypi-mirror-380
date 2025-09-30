#!/usr/bin/env bash
# done: 如何检测脚本是否被source, 如果不是source, 就退出.

if ! [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
   echo "script ${BASH_SOURCE[0]} should be sourced"
   exit 0
fi

# todo:检查和安转依赖, 也许需要另起一个脚本. 或者用make. 另外source部分直接用virtualenv试试

# 建立并激活虚拟环境, 安装依赖, 设置环境变量.


# 设置环境变量
export PYTHONPATH=$(pwd):$PYTHONPATH
# export PYTHONPATH=~/_env/lib/general:$PYTHONPATH

# 安装virtualenvwrapper, autoenv, 切换env环境
pip install virtualenvwrapper autoenv
source virtualenvwrapper.sh
# pip install percol invoke autopep8 isort

if [ -f ~/anaconda2 ]; then
  mv ~/anaconda2/bin/deactivate ~/anaconda2/bin/conda-deactivate
fi
if [ -f ~/anaconda ]; then
  mv ~/anaconda/bin/deactivate ~/anaconda/bin/conda-deactivate
fi

# 设置virtualenv
mkvirtualenv labkit
workon labkit


# 安装所有依赖
# pip install pip-tools
# pip-compile
# pip-sync
pip install -r requirements.txt
