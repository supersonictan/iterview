cmake_minimum_required(VERSION 3.6)
project(CCode)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp practise.cpp)

add_executable(CCode ${SOURCE_FILES})