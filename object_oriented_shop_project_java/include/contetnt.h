<<<<<<< HEAD
//
// Created by mikolaj on 10.01.2023.
//

#include <string>
#include <list>

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
    virtual float price();
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
    list<Product> items;
    float worth;

    virtual Cart* addItem(Product item)=0;
    virtual Cart* removeItem(int n)=0;
};

class ShoppingCart: public Cart{
public:
    ShoppingCart(list<Product> l, float w);
    ShoppingCart* addItem(Product item);
    ShoppingCart* removeItem(int n);
    //ShoppingCart* clear();
    //void displayCart();
};

=======
//
// Created by mikolaj on 10.01.2023.
//

#include <string>

#ifndef PROJECT_2_CONTETNT_H
#define PROJECT_2_CONTETNT_H

#endif //PROJECT_2_CONTETNT_H

using namespace::std;

class Productable{
public:
    string name;
    int amount;
    float price;

    virtual Productable* takeProduct() = 0;
};

class Product: public Productable{
public:
    Product(string n, int a, float p);
    Product* takeProduct();
    Product makeDiscount(float new_price);
};

>>>>>>> 2ce731aa28992a4b448bea9cec737bcb6154872f
