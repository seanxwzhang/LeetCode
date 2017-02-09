cmake_minimum_required(VERSION 3.6)
project(LeetCode)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Werror")

set(SOURCE_FILES "033 Search in Rotated Sorted Array/solution.cpp")

add_executable(go ${SOURCE_FILES})

