
//
// Created by mikolaj on 10.01.2023.
//

#include <string>
#include <list>
#include <vector>

#ifndef PROJECT_2_CONTETNT_H
#define PROJECT_2_CONTETNT_H

#endif //PROJECT_2_CONTETNT_H

using namespace::std;

class Productable{
public:
    string name;
    int amount;
    float _price;

    virtual Productable* takeProduct() = 0;
    virtual float price() = 0;
};

class Product: public Productable{
public:
    Product(string n, int a, float p);
    Product* takeProduct();
    Product makeDiscount(float new_price);
    float price();
};

class Cart{
public:
    vector<Product> items;
    float worth;

    virtual Cart* addItem(Product item)=0;
    virtual Cart* removeItem(int n)=0;
};

class ShoppingCart: public Cart{
public:
    bool active;
    ShoppingCart();
    ShoppingCart(vector<Product> i, int w);
    ShoppingCart* addItem(Product item);
    ShoppingCart* removeItem(int n);
    ShoppingCart* clear();
    ShoppingCart* enterCart();
    void closeCart();
    void refreshCartDisplay();
    ShoppingCart* handleEvents(int buf);
    ShoppingCart* new_cart;
};

class Store{
public:
    vector<Product> warehouse;
    ShoppingCart* cart;
    string name;

    virtual void enterShop() = 0;
    virtual void purchase() = 0;
    virtual void closeShop() = 0;
};

class FakeShop: public Store{
public:
    bool active;
    ShoppingCart* cart;
    FakeShop(string n, vector<Product> w);
    void handleEvents(string buf);
    void enterShop();
    void purchase();
    void closeShop();
    void refresh();
};