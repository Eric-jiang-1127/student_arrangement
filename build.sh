#!/bin/bash

# 创建build目录
mkdir -p build
cd build

# 运行cmake和make
cmake ..
make

cd ..
# 确保data目录存在
mkdir -p data

# 编译完成后自动运行
if [ -f ./build/studentarrangement ]; then
    echo "====== 运行结果 ======"
    ./build/studentarrangement
fi