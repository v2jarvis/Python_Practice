#practice on pickling and unpickiling
import pickle

#Object to pickle
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

#Pickle the object
val=open('data2.pkl', 'wb')
pickle.dump(data,val)

#Unpickle the object
val=open('data2.pkl', 'rb')
loaded_data = pickle.load(val)
print(loaded_data)
