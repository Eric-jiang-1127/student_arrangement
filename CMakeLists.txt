cmake_minimum_required(VERSION 3.10)
project(studentarrangement C)

add_executable(studentarrangement src/main.c src/showinfo.c src/edit_stu.c src/sort.c src/search.c)

target_include_directories(studentarrangement PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
