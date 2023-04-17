#include <iostream>
#include "D:\git_repos\oop-put-course\project-2\include\content.h"
using namespace::std;

int main() {
    Product* p1 = new Product("keyboard", 10, 100);
    Product* p2 = new Product("mouse", 2, 150);
    Product* p3 = new Product("TV", 2, 150);
    Product* p4 = new Product("screen", 2, 150);

    vector<Product> warehouse = {*p1, *p2, *p3, *p4};

    FakeShop shop = FakeShop("mujsklep", warehouse);

    shop.enterShop();

    return 0;
}