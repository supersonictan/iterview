cmake_minimum_required(VERSION 3.6)
project(CCode)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        list.cpp test.cpp sort.cpp)

add_executable(CCode ${SOURCE_FILES})