# Conditional Tests: Write a series of conditional tests. Print a
# statement describing each test and your prediction for the results of
# each test. Your code should look something like this:
# car = 'subaru'
# print ("Is car == 'subaru'? I predict True.")
# print (car == 'subaru')

beer = 'Coors Light'
print ("beer = 'Coors Light'")
print("Is beer == 'Coors Light'? I preduct True.", beer == 'Coors Light')
print("Is beer == 'coors light'? I predict False.", beer == 'coors light')
print("Is beer.lower() == 'coors light'? I predict True.", beer.lower() == 'coors light')

beer_01 = 'Coors Light'
beer_02 = 'Cumbre'
print("beer_01 = 'Coors Light', beer_02 = 'Cumbre'")
print("beer_01 == 'Coors Light' and beer_02 == 'Cumbre'? I predict True.", beer_01 == 'Coors Light' and beer_02 == 'Cumbre')
print("beer_01 == 'Coors light' and beer_02 == 'Cumbre'? I predict False.", beer_01 == 'Coors light' and beer_02 == 'Cumbre')
print("beer_01 == 'Coors Light' or beer_02 == 'Lagunitas'? I predict True.", beer_01 == 'Coors Light' or beer_02 == 'Lagunitas')
print("beer_01 == 'coors light' or beer_02 == 'cumbre'? I predict False.", beer_01 == 'coors light' or beer_02 == 'cumbre')