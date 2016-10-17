cmake_minimum_required(VERSION 3.6)
project(LeetCode)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Werror")

set(SOURCE_FILES test.cpp)

add_executable(go ${SOURCE_FILES})

add_executable(solution best_time_to_buy_and_sell_stock/solution.cpp)
