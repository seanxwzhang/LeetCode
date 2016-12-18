cmake_minimum_required(VERSION 3.6)
project(LeetCode)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Werror")

set(SOURCE_FILES "013 Roman to Integer/solution.cpp")

add_executable(go ${SOURCE_FILES})

