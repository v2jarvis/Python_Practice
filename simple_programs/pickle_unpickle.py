#pickling and unpickling in python
import pickle

#data = {'name': 'John', 'age': 30, 'city': 'New York'}

#with open('data.pickle', 'wb') as file:
#    pickle.dump(data, file)

with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
