#perform tghe multiple tadk on dict using there method.
'''car = {
  "brand": "Bugati",
  "model": "Mustang",
  "year": 1964,
  "value": 1.20
}

car.update({"model": "Ceron","year":2020}) #update the key and value.
print(car.get('year')) #get the value using key.
print(car.items()) #return a tupple with list and tupple pair.
print(car.pop("year")) #pop the item using key.
print(car.popitem())  #pop item last add value remove and return the tuple.
print(car.keys()) #return the tupple in list the keys.
print(car.values()) #return the tupple in the list values.
print(car)'''
a=('1','2','3','4')
b=('niteesh')
d1=dict.fromkeys(a,b)
print(d1)