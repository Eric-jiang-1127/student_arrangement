cmake_minimum_required(VERSION 3.10)
project(studentarrangement C)

add_executable(studentarrangement src/main.c src/showinfo.c src/edit_stu.c src/sort.c src/search.c src/sqlite.c)

target_link_libraries(studentarrangement sqlite3)

target_include_directories(studentarrangement PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
