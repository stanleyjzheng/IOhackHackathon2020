#We need to find a way to search for the user to search for a place with Google's autofill, let's assume it's called userPlaceID. Also an input from the user that gives userRadius, and userLocation. 
import populartimes as pt
import math

userLocation = [] #Formated as [latitude, longitude]. Searches within the nearest userRadius kilometers. USER INPUT
userRadius = int() #Radius user would like to search within in KM. USER INPUT
userTypes = []
userPlaceID = str() #MAKE SURE IS STRING! USER INPUT
userPlaceStorage = []
singleUserTypes = 'placeholder'
coord1 = 1
coord2 = 2
coord3 = 3
coord4 = 4
first = [] #Reccomended store
APIKey = 'AIzaSyByaR7_Gekvt_R5tGrs260PXf1OkzF9T9s'
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4]) #Create an ordinal of any number eg. ordinal(5) outputs 5th
placeStorage = []#Similar dictionary
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
    global userPlaceStorage
    global coord1
    global coord2
    global coord3
    global coord4
    global APIKey
    global userPlaceID
    global placeStorage
    global userLocation
    global placeID
    global name
    global address
    global types
    global current_popularity
    global international_phone_number

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

'''The Bownesian Grocer , is the least busy grocery or supermarket in the radius of 7 km, and is at 45 % of peak volume (live)
other nearby
the 2nd least busy supermarket called E-Mart is at 51 % of peak volume (live)
the 3rd least busy supermarket called Koreana Market is at No data % of peak volume (live)   
the 4th least busy supermarket called Handee Food Store is at No data % of peak volume (live)
the 5th least busy supermarket called One Way Foods is at No data % of peak volume (live)    
the 6th least busy grocery_or_supermarket called FOOD WORLD Halal meat and grocery is at No data % of peak volume (live)
the 7th least busy grocery_or_supermarket called M&M Food Market is at No data % of peak volume (live)
the 8th least busy supermarket called Indian Aroma Halal Grocery Store is at No data % of peak volume (live)
the 9th least busy grocery_or_supermarket called Maple Leaf No.2 Food Market is at No data % of peak volume (live)
the 10th least busy grocery_or_supermarket called M&M Food Market is at No data % of peak volume (live)
the 11th least busy store called Kalamata is at No data % of peak volume (live)
the 12th least busy supermarket called Little Green Mart is at No data % of peak volume (live)
the 13th least busy supermarket called Shaganappi Grocery Store is at No data % of peak volume (live) first use used 3130 API keys.'''

# "C:/Users/Stanley Zheng/Anaconda3/python.exe" z:/Backend/popular-times.py
'''File "z:/Stanley/stanminitest.py", line 59, in <module>
    minimumCurrentPopularity = min(current_popularity)
ValueError: min() arg is an empty sequence so we need to put it into a '''