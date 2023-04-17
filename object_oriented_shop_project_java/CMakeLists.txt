cmake_minimum_required(VERSION 3.24)
project(project_2)

set(CMAKE_CXX_STANDARD 17)

add_executable(project_2 src/main.cpp include/content.h src/content/Product.cpp src/content/ShoppingCart.cpp src/content/FakeShop.cpp)

