import populartimes as pt
#Use this program if you would like to make a cache of a pt command
APIKey = 'AIzaSyByaR7_Gekvt_R5tGrs260PXf1OkzF9T9s'
userRadius = 7#(int) for the # of kms you want to search from. Must be under 7 for a Google API free trial
userLocation = [51.043321, -114.067825] #[latitude, longitude] of where you want to search from. 
coord1 = userLocation[0] - 0.00904371733*userRadius #Calculate 4 corners of coordinates from the 
coord2 = userLocation[1] - 0.00904371733*userRadius #One km is 0.00904371733 degree of latitude or longitude 
coord3 = userLocation[0] + 0.00904371733*userRadius
coord4 = userLocation[1] + 0.00904371733*userRadius
singleUserType = 'grocery_or_supermarket' #(str) Search for this category of store. More can be viewed at https://developers.google.com/places/supported_types

placeStorage = pt.get(APIKey, [singleUserType], (coord1, coord2), (coord3, coord4)) #Get the places from google API

f = open("onlinecache.txt", "w")
f.write(str(placeStorage))
f.close()

f = open("onlinecache.txt", "r")
print(f.read())
f.close() #For the current onlinecache.txt, this was run on 2020-05-31 at 11:09AM. 