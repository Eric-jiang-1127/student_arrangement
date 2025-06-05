cmake_minimum_required(VERSION 3.10)
project(studentarrangement C)

add_executable(test_showmenu src/test_main.c src/showinfo.c src/edit_stu.c)

target_include_directories(test_showmenu PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
