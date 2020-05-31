import populartimes as pt
import math

#WORKING OFFLINE PROTOTYPE
userLocation = [51.088516, -114.146796] #Formated as [latitude, longitude]. Searches within the nearest userRadius kilometers. USER INPUT
userRadius = int(7) #Radius user would like to search within in KM. USER INPUT
userTypes = ['grocery_or_supermarket']
userPlaceID = str('ChIJM94LKJdocVMRKFF10w4rKDg') #MAKE SURE IS STRING! USER INPUT
coord1 = 1 
coord2 = 1  
coord3 = 1
coord4 = 1
singleUserTypes = 'placeholder'
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])
#placeStorage = []#Similar dictionary
placeStorage = [{'id': 'ChIJu6-a3lZwcVMRsaQZjVvUv0w', 'name': "O'Sullivan's Restaurant & Bar", 'address': '5809 Macleod Trail Southwest, Calgary', 'types': ['bar', 'restaurant', 'food', 'point_of_interest', 'establishment'], 'coordinates': {'lat': 51.0015969, 'lng': -114.0723563}, 'rating': 3.8, 'rating_n': 407, 'populartimes': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 
9, 17, 27, 38, 49, 57, 60, 57, 45, 28, 14]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 7, 12, 17, 22, 25, 26, 25, 21, 16, 11, 7]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 7, 11, 17, 30, 43, 48, 40, 30, 25, 17, 7]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 10, 7, 8, 14, 21, 29, 33, 34, 30, 23, 15, 9]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 11, 18, 26, 33, 41, 50, 64, 79, 89, 94, 100, 96]}, {'name': 'Saturday', 'data': [72, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9, 15, 21, 21, 18, 18, 27, 45, 57, 51, 39]}, {'name': 'Sunday', 'data': [47, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 13, 22, 31, 38, 44, 48, 47, 39, 27, 14]}], 'time_spent': [60, 120]}, {'id': 'ChIJd5hk0_1wcVMRRkZNLvZ43Qc', 'name': "Smuggler's Inn", 'address': '6920 Macleod Trail S, Calgary', 'types': ['bar', 'restaurant', 'food', 'point_of_interest', 'establishment'], 'coordinates': {'lat': 50.99198599999999, 'lng': -114.0709059}, 'rating': 4.4, 'rating_n': 1616, 'populartimes': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 23, 30, 24, 13, 14, 32, 55, 
61, 42, 0, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 31, 34, 23, 11, 14, 33, 55, 59, 40, 0, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 29, 32, 16, 9, 19, 38, 55, 57, 41, 0, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 35, 39, 18, 8, 19, 47, 74, 76, 52, 0, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 46, 47, 28, 17, 29, 58, 88, 100, 84, 52, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 27, 61, 67, 37, 0, 0, 40, 64, 84, 94, 84, 53, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 49, 77, 79, 53, 0, 0, 27, 60, 94, 99, 70, 0, 0, 0]}], 'time_wait': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 15, 30, 15, 15, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 0, 0, 0, 0, 15, 15, 15, 0, 0, 0]}], 'time_spent': [120, 120]}, {'id': 'ChIJd5hk0_1wcVMRcdY2O8RbQYI', 'name': 
'Bolero', 'address': '6920 Macleod Trail S, Calgary', 'types': ['bar', 'restaurant', 'food', 'point_of_interest', 'establishment'], 'coordinates': {'lat': 50.9922222, 'lng': -114.0708332}, 'rating': 4.5, 'rating_n': 1208, 'populartimes': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 31, 39, 29, 0, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 29, 38, 29, 0, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 37, 48, 30, 0, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 40, 44, 30, 0, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 76, 100, 89, 55, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 63, 83, 87, 89, 69, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 14, 38, 62, 65, 43, 0, 0, 0]}], 'time_wait': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 0, 0, 0, 0, 15, 15, 15, 0, 0, 0]}], 'time_spent': [120, 120]}, {'id': 'ChIJo_ttg_lwcVMRwI-VL8pubAI', 'name': 'Mariposa Saloon', 'address': '6008 Macleod Trail Southwest #109, Calgary', 'types': ['night_club', 'bar', 'point_of_interest', 'establishment'], 'coordinates': {'lat': 50.9995634, 'lng': -114.0707021}, 'rating': 4.0, 'rating_n': 83, 'populartimes': [{'name': 'Monday', 'data': [31, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 9, 11, 15, 20, 21, 22]}, {'name': 'Tuesday', 'data': [27, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 11, 16, 20, 22, 24, 26, 30]}, {'name': 'Wednesday', 'data': [29, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 8, 11, 13, 18, 30, 38, 31]}, {'name': 'Thursday', 'data': [28, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 9, 16, 24, 32, 37, 45, 59]}, {'name': 'Friday', 'data': [66, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 20, 29, 38, 44, 53, 69, 91]}, {'name': 'Saturday', 'data': [100, 81, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 18, 14, 11, 27, 60, 78, 80]}, {'name': 'Sunday', 'data': [96, 96, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 12, 20, 27, 30, 30]}]}, {'id': 'ChIJKXxPq_hwcVMREy656Ymom4s', 'name': 'Red Lobster', 'address': '100-6100 Macleod Trail Southwest, Calgary', 'types': ['bar', 'restaurant', 'food', 'point_of_interest', 'establishment'], 'coordinates': {'lat': 50.99855700000001, 'lng': -114.070882}, 'rating': 4.1, 'rating_n': 1929, 'populartimes': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 18, 19, 14, 11, 20, 35, 44, 41, 28, 0, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 13, 15, 13, 15, 27, 46, 56, 48, 28, 0, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 15, 17, 12, 8, 13, 29, 43, 39, 23, 0, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 17, 22, 16, 12, 22, 44, 63, 59, 38, 0, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 25, 31, 18, 16, 36, 66, 84, 82, 64, 38, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 22, 39, 47, 47, 57, 81, 100, 92, 62, 31, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 17, 30, 34, 35, 47, 64, 70, 57, 34, 0, 0, 0]}], 'time_wait': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 15, 15, 0, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 15, 30, 30, 15, 15, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 0, 0, 0]}], 'time_spent': [60, 120]}, {'id': 'ChIJM94LKJdocVMRKFF10w4rKDg', 'name': 'Real Canadian Superstore', 'address': '5251 Country Hills Blvd NW, Calgary, AB T3A 5H8, Canada', 'types': ['grocery_or_supermarket', 'pharmacy', 'bakery', 'food', 'health', 'point_of_interest', 'store', 'establishment'], 'coordinates': {'lat': 51.13645880000001, 'lng': -114.1612333}, 'rating': 4.0, 'rating_n': 2363, 'international_phone_number': '+1 403-241-4027', 'current_popularity': 42, 'populartimes': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 16, 27, 39, 49, 56, 60, 63, 65, 67, 66, 60, 49, 37, 24, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 18, 27, 36, 44, 50, 55, 58, 61, 62, 59, 51, 40, 28, 17, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 12, 19, 26, 32, 37, 41, 45, 48, 50, 48, 42, 34, 25, 16, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 16, 25, 34, 41, 45, 47, 49, 52, 55, 55, 51, 43, 32, 20, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 19, 33, 44, 50, 53, 58, 66, 71, 72, 69, 64, 54, 40, 26, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 21, 43, 67, 83, 88, 88, 90, 93, 88, 77, 62, 49, 36, 23, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 18, 36, 58, 77, 89, 96, 99, 100, 93, 80, 63, 46, 31, 20, 0, 0]}], 'time_spent': [20, 60]}]

placeID = [] #PlaceID from placeStorage
name = [] #Name from placeStorage
address = [] #Address from placeStorage
types = [] #Type of place/business from placeStorage
international_phone_number = [] #Phone number from placeStorage
current_popularity = [] #Current popularity as a % of peak from placeStorage

def similarLocations():
    global userTypes
    global userRadius
    global singleUserTypes
#    global userPlaceStorage ONLINE API SERVICE ONLY
    global coord1
    global coord2
    global coord3
    global coord4
#    global APIKey ONLINE API SERVICE ONLY
    global userPlaceID
    global placeStorage
    global userLocation
    global placeID
    global name
    global address
    global types
    global current_popularity
    global international_phone_number
    '''
    #ONLINE API SERVICE ONLY
    userPlaceStorage = pt.get_id(APIKey, userPlaceID) 


    #Extra types deletion. We need to remove some categories since they are too prevalent, and would result in thousands of results.
    userTypes = userPlaceStorage['types'] 
    for a in userTypes:
        if a == 'point_of_interest':
            userTypes.remove('point_of_interest')
        if a == 'store':
            userTypes.remove('store')
        if a == 'establishment':
            userTypes.remove('establishment')
        if a == 'intersection':
            userTypes.remove('intersection')
    singleUserTypes = str(userTypes[0])


    #placeStorage = pt.get(APIKey, [singleUserTypes], (coord1, coord2), (coord3, coord4), 20, 1, False) #pt.get a list of businesses with the same user specified type and within a user specified radius from their location. 
    if userRadius > 7:
        userRadius = 7 #If the user sets a radius of more than 7, set the radius to 7 (otherwise there will be too many results.)

    userLocation = []
    userLocation = userPlaceStorage['coordinates']
    userLat = userLocation['lat']
    userLong = userLocation['lng']
    userLocation = []
    userLocation.append(userLat)
    userLocation.append(userLong)
    coord1 = userLocation[0] - 0.00904371733*userRadius 
    coord2 = userLocation[1] - 0.00904371733*userRadius #One km is 0.00904371733 degree of latitude or longitude 
    coord3 = userLocation[0] + 0.00904371733*userRadius
    coord4 = userLocation[1] + 0.00904371733*userRadius
    print(singleUserTypes)
    print(userTypes)
    placeStorage = pt.get(APIKey, [singleUserTypes], (coord1, coord2), (coord3, coord4)) #pt.get a list of businesses with the same user specified type and within a user specified radius from their location. 
    print(placeStorage)
    ''' # ONLINE API SERVICE ONLY
    index = 0
    while index < len(placeStorage):#Runs through entire placeStorage
        placeID.append(placeStorage[index]['id'])#Append a ton of information to respective lists
        name.append(placeStorage[index]['name'])
        address.append(placeStorage[index]['address'])
        types.append(placeStorage[index]['types']) 
        if 'current_popularity' in placeStorage[index]:#If the dictionary has current_popularity
            current_popularity.append(placeStorage[index]['current_popularity'])#Append it to current_popularity the list.
        else: 
            current_popularity.append(101)#If not, make it 101.
        if 'international_phone_number' in placeStorage[index]:
            international_phone_number.append(placeStorage[index]['international_phone_number'])
        else:
            international_phone_number.append('No data')
        index += 1#Increments the index by 1 to repeat this for the next dictionary.
    userTypes = [x.replace('_', ' ') for x in userTypes] #Replace underscores throughout with spaces for beauty


def indexSort():
    global current_popularity
    global placeID
    global name
    global address
    global international_phone_number
    global types
    global userRadius

    current_popularity, placeID, name, address, types, international_phone_number = (list(t) for t in zip(*sorted(zip(current_popularity, placeID, name, address, types, international_phone_number))))
    
    types = [[x.replace('_',' ') for x in l] for l in types]
    
    for n, i in enumerate(current_popularity):
        if i == 101:
            current_popularity[n] = 'No data'

    for a in types:#We need to remove some categories since they are too prevalent, and would result in thousands of results.
        if a == 'health':
            types.remove('health')
        if a == 'point of interest':
            types.remove('point of interest')
        if a == 'store':
            types.remove('store')
        if a == 'establishment':
            types.remove('establishment')
        if a == 'intersection':
            types.remove('intersection')


def nodeReturn():
    print(len(current_popularity))#Know how many 4 line segments to expect
    index3 = 0
    while index3 < len(current_popularity):
        busyNumber = index3 + 1
        print(ordinal(busyNumber)) #Position (2nd least busy, 3rd least buys, etc)
        print(types[index3][0])  #Type of business, bar, grocery or supermarket, etc.
        print(name[index3]) #Name of business
        print(current_popularity[index3]) #Current popularity as a % of peak. Shows 'No data' if there is no data. 
        index3 += 1


def main():
    similarLocations()
    indexSort()
    nodeReturn()


if __name__ == "__main__":
    main() #execute main