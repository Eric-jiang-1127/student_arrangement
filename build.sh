#!/bin/bash

# 创建build目录
mkdir -p build
cd build

# 运行cmake和make，自动编译test_main.c相关目标
cmake ..
make

# 编译完成后自动运行
if [ -f ./studentarrangement ]; then
    echo "====== 运行结果 ======"
    ./studentarrangement
fi