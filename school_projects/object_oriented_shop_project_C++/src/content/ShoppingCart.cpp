#include <iostream>
#include <stdlib.h>
#include "D:\git_repos\oop-put-course\project-2\include\content.h"
using namespace::std;

ShoppingCart::ShoppingCart() {
    this->items = {};
    this->worth = 0;
}
ShoppingCart::ShoppingCart(vector<Product> i, int w) {
    this->items = i;
    this->worth = w;
}

ShoppingCart *ShoppingCart::addItem(Product item) {
    if(item.amount <= 0){
        throw "Can not add item to the cart - item out of stock";
    }else {
        vector<Product> new_items = this->items;
        new_items.push_back(item);
        return new ShoppingCart(new_items, this->worth + item.price());
    }
}

ShoppingCart *ShoppingCart::removeItem(int n) {
    vector<Product> new_items = this->items;
    vector<Product>::iterator item = std::next(new_items.begin(), n-1);
    float new_worth = this->worth - item->price();
    new_items.erase(item);
    return new ShoppingCart(new_items, new_worth);
}

ShoppingCart *ShoppingCart::clear() {
    return new ShoppingCart();
}

ShoppingCart* ShoppingCart::enterCart() {
    this->active = true;
    int buf;
    this->new_cart = new ShoppingCart(this->items, this->worth);
    while(this->active){
        new_cart->refreshCartDisplay();
        cin>>buf;
        new_cart = this->handleEvents(buf);
    }
    return new_cart;
}

void ShoppingCart::refreshCartDisplay() {
    cout<<"\nCART";
    cout<<"\nchoose number to delete item or press 0 to exit cart"<<endl;
    int n = this->items.size();
    for(int i=0; i<n; i++){
        Product item = this->items.at(i);
        cout<<"\n"<<i+1<<" "<<item.name<<" price: "<<item._price<<endl;
    }
}

void ShoppingCart::closeCart() {
    this->active = false;
}

ShoppingCart* ShoppingCart::handleEvents(int buf) {
    if(buf == 0){
        this->closeCart();
        return this->new_cart;
    }
    else return this->new_cart->removeItem(buf);
}