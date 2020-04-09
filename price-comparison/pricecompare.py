# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import operator


#amazon_url= 'http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='
flipkart_url = 'https://www.flipkart.com/search?q='
snapdeal_url = 'https://www.snapdeal.com/search?keyword='
keyword = input('Enter the Product Name:: - ').split()
for item in keyword:
   # amazon_url += item+'+'
    flipkart_url += item+'%20'
    snapdeal_url += item+'%20'
#amazon_url = amazon_url[:-1]
flipkart_url = flipkart_url[:-3]
snapdeal_url = snapdeal_url[:-3]


def print_flipkart(products,price):
    products = products[0:3]
    price = price[0:3]
    results = []
    
#     print(l.text)
    for item, money in zip(products, price):
        results.append([item.text, money.text])
    print(tabulate(results, headers=["Product on Flipkart", "Price"], tablefmt="fancy_grid"))
def flipkart(url):
        source = requests.get(url).content
        soup = BeautifulSoup(source, 'lxml')
        products = soup.findAll('a',{'class':'_2cLu-l'})
        price = soup.findAll("div",{"class":"_1vC4OE"})
        k=price[0]
        if (len(products) > 0 and len(price) > 0):
            print_flipkart(products,price)
        else:
            products = soup.findAll('a',{'class':"._3wU53n"})
            price = soup.findAll("div",{"class":"._1vC4OE._2rQ-NK"})
           
            if(len(products) > 0 and len(price) > 0):
                print_flipkart(products,price)
            else:
                print("Flipkart does not sell this product.\n")
        return k.text
    
def snapdeal(url):
    global m
    m=[]
    try:
        source = requests.get(url).content
        soup = BeautifulSoup(source, 'lxml')
        products = soup.find_all("p", {"class": "product-title"})
        price = soup.find_all("span", {"class": "lfloat product-price"})
        if(len(products)>0 and len(price)>0):
            products = products[0:3]
            price = price[0:3]
            m=price[0].text
            results = []
            for item, money in zip(products, price):
                results.append([item.string, money.text])
            print(tabulate(results, headers=["Product on Snapdeal", "Price"], tablefmt="fancy_grid"))
        else:
            print("SnapDeal does not sell this product.\n")
    except:
        print(" Please check your internet connection and try again\n.")
    return m

def amazon(url):
    global z
    z=[]
    try:
        source = requests.get(url).content
        soup = BeautifulSoup(source,'lxml')
        products = soup.find_all("a",{"class":"a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
        price = soup.find_all("span", {"class": "a-size-base a-color-price s-price a-text-bold"})
        if(len(products)>0 and len(price)>0):
            products = products[0:3]
            price = price[0:3]
            z=price[0].text
            results = []
            for item,money in zip(products,price):
                results.append([item.string,money.text])
            print(tabulate(results, headers=["Products on Amazon", "Price"], tablefmt="fancy_grid"))
        else:
            print("Amazon does not sell this product.\n")
    except:
        print("An error occured while loading the webpage. Please check your internet connection and try again.\n")
    return z
        
        
def compare():
    a=[]
    k=[]
    final=[]
    d=[]
    sorted_dict={}
    m=snapdeal(snapdeal_url)
   # z=amazon(amazon_url)
    l=flipkart(flipkart_url)
    a=a+[l[1:],m[5:]]
    #a.append(z[2:])
    j=0
    for i in a:
        m=i.split(',')
        i=''.join(m)
        k.append(i)
    for i in k:
        j=float(i)
        final.append(j)
    l=['Flipkart','Snapdeal']
    d=dict(zip(l,final))
    sorted_dict= sorted(d.items(), key=operator.itemgetter(1))
    print("Best Price::",sorted_dict[0])    
compare()
