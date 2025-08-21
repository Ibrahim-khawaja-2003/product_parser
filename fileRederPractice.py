import json
import os
import requests

url = 'https://dummyjson.com/products'
# requests.get
# response.json
r = requests.get(url)
# print(r)
results = r.json()
# print(data)

# with open("./products.json", "r") as f:
#     results  = json.load(f)

def printProductInfo(infoTitle):
                
        for i in range(len(results["products"])):
            print(results["products"][i][infoTitle])

        os.system('pause')
        os.system('cls')

def printCategoryProducts(category):
        
        for i in range(len(results["products"])):
            if results["products"][i]["category"] == category:
                print(results["products"][i]["title"])
        
        os.system('pause')
        os.system('cls')


def printSummary():

    sumTotalPrice = 0
    sumTotalDiscount = 0
    sumTotalDifference = 0
    
    for product in results["products"]:
    
        sumTotalPrice = sumTotalPrice + product["price"]
        sumTotalDiscount = sumTotalDiscount + product["price"]*product["discountPercentage"]/100
        sumTotalDifference = sumTotalDifference + (product["price"] - product["price"]*product["discountPercentage"]/100)
    
        print("Title: ", product["title"])
        print("Price: ", product["price"])
        print("Discount: ", product["discountPercentage"], "%")
        print("Discount in Rs: ", product["price"]*product["discountPercentage"]/100)

        print("--------------------------------")
        print(sumTotalPrice)
        print(sumTotalDiscount)
        print(sumTotalDifference)
        print("--------------------------------")
    
    os.system('pause')
    os.system('cls')

def infoPrint():
    choice = input("""
                Please select what kind of information you want?
                   1- id
                   2- title
                   3- description
                   4- category
                   5- discountPercentage
                   6- rating
                   7- stock
                   => """)
    
    printProductInfo(choice)

def categoryWiseInfo():
    choice = input("""
                Please select the category:
                   1- beauty
                   2- fragrances
                   3- furniture
                   4- groceries
                   => """)
    
    printCategoryProducts(choice)

def main():

    print("Welcome to Products details")
    while(True):
        print("""Select Options:
            1- Specific Information of Products (Press 1)
            2- Summary Analysis (Press 2)
            3- Category Wise Title of Products (Press 3)
            4- Quit (Press Anyother)
            """)
        choiceOne = input("Enter Choice: ")
        if choiceOne == "1":
            infoPrint()
        elif choiceOne == "2":
            printSummary()
        elif choiceOne == "3":
            categoryWiseInfo()
        else:
            print("Thanks for Using")
            return

main()