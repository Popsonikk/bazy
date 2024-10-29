import pymongo
import pprint
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.restaurant
coll = db.restaurants
while True:
    option=int(input("Podaj numer:\n1.Znajdź dokument\n2.Wstaw dokument\n3.Edytuj dokument\n4.Usuń dokument\n5.Zakończ\n"))
    match option:
        case 1:
            field=input("Podaj pole: ")
            value=input("Podaj wartość: ")
            toFind = {field:value}
            result = coll.find_one(toFind)
            pprint.pprint(result)
        case 2:
            name=input("Podaj nazwę: ")
            borough=input("Podaj dzielnice: ")
            cuisine=input("Podaj kuchnię: ")
            new_doc={ "name":name,"borough":borough,"cuisine":cuisine}
            result = coll.insert_one(new_doc)
            pprint.pprint(result)    
        case 3:
            field=input("Podaj pole: ")
            value=input("Podaj wartość: ")
            operator=input("Podaj operator: ")
            update_field = input("Podaj pole do zaktualizowania: ")
            update_value=input("Podaj wartość do zaktualizowania: ")
            toFind = {field:value}
            toUpdate = {operator:{update_field:update_value}}
            result = coll.update_one(toFind,toUpdate)
            pprint.pprint(result)
        case 4:
            field=input("Podaj pole: ")
            value=input("Podaj wartość: ")
            toDelete = {field:value}
            result = coll.delete_one(toDelete)
            pprint.pprint(result)
        case 5:
            print("Koniec programu")
            break









