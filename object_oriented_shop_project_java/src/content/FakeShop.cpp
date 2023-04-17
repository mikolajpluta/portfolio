#include "D:\git_repos\oop-put-course\project-2\include\content.h"
#include <iostream>
#include <stdlib.h>
using namespace::std;

FakeShop::FakeShop(string n, vector<Product> w) {
    this->name = n;
    this->warehouse = w;
    this->cart = new ShoppingCart();
}
void FakeShop::enterShop() {
    this->active = true;
    string buf;
    while(this->active){
        this->refresh();
        cin>>buf;
        this->handleEvents(buf);
    }
}
void FakeShop::closeShop() {
    this->active = false;
}
void FakeShop::purchase() {
    this->closeShop();
    cout<<"payment compleeted, thank You for shopping!";
    this->active = false;
}
void FakeShop::handleEvents(string buf) {
    int buf_int;
    if(buf == "01"){
        this->cart = this->cart->enterCart();
    }else if(buf == "02"){
        this->purchase();
    }else if(buf == "03"){
        this->closeShop();
    }else{
        buf_int = stoi(buf);
        try{
            this->cart = this->cart->addItem(this->warehouse.at(buf_int - 1));
            this->warehouse.at(buf_int - 1).amount -= 1;
        }catch (const char* msg){
            cerr << msg << endl;
        }
    }
}

void FakeShop::refresh() {
    cout<<"welcome to the "<<this->name<<endl;
    cout<<"choose number to add product to the shop or select action\n";
    int n = this->warehouse.size();
    for(int i=0; i<n; i++){
        Product item = this->warehouse.at(i);
        cout<<i+1<<" "<<item.name<<" price: "<<item._price<<" in stock: "<<item.amount<<endl;
    }
    cout<<"\n\n01 - enter shopping cart ("<<this->cart->items.size()<<")";
    cout<<"\n02 - purchase";
    cout<<"\n03 - exit\n";
}