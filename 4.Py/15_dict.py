capitals = {
    'India' : 'New Delhi', 
    'Canada' : 'Ottawa',
    'USA' : "Washington DC"
}

print(capitals['India'])
print(capitals.get('India'))

keys = capitals.keys()
print('Keys : ', keys)

for key, val in capitals.items():
    print(f'{key} : {val}')

