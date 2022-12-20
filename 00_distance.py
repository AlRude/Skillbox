#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
cities = []
counter = 0

for city in sites.keys():
    cities.append(city)

#print(cities)
#print(len(cities))

for city in cities:
    distances[city] = {}

    while counter < len(cities):
        if cities[counter] == city:
            pass
        else:
            x1, y1 = sites[city]
            x2, y2 = sites[cities[counter]]
            distances[city][cities[counter]] = (x1 - x2) ** 2 + (y1 - y2) ** 2
        counter += 1
    #if counter == len(cities)-1 :
        #x1, y1 = sites[cities[counter]]
        #x2, y2 = sites[cities[0]]
        #distance_name = str(cities[counter]+'_'+cities[0])
        #distances[cities[counter]][cities[0]] = (x1 - x2) ** 2 + (y1 - y2) ** 2
    #else:
        #x1, y1 = sites[cities[counter]]
        #x2, y2 = sites[cities[counter+1]]
        #distance_name = str(cities[counter]+'_'+cities[counter+1])
        #distances[cities[counter]][cities[counter+1]] = (x1 - x2) ** 2 + (y1 - y2) ** 2

    #distances[cities[counter]][cities[0]] = (x1 - x2) ** 2 + (y1 - y2) ** 2
    #counter += 1


# TODO здесь заполнение словаря

print(distances)




