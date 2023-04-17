//
// Created by mikolaj on 10.01.2023.
//
#include "D:\git_repos\oop-put-course\project-2\include\content.h"
using namespace::std;

Product::Product(string n, int a, float p) {
    this->name = n;
    this->amount = a;
    this->_price = p;
}

Product *Product::takeProduct() {
    Product* new_product =  new Product(this->name, this->amount-1, this->_price);
    return new_product;
}

Product Product::makeDiscount(float new_price) {
    return Product(this->name, this->amount, new_price);
}

float Product::price() {
    return this->_price;
}