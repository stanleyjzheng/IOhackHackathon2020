# IOhackHackathon2020 (PopQ!)
  PopQ! by BLACKPINK

  PopQ!, or popular times and queue, is an all-in-one webpage designed for facilitating social distancing by directing users to less busy stores as well as providing a remote queue system so that users may stay in their cars while waiting for busy services.

# pt (populartimes)
  The goal of this program is to give users advice in order to avoid crowds at stores and public places. 
  From a user provided store and radius, PopQ! searches the area for similar stores that have the lowest live volume using Google's    popular times API. 
  
  onlinetest.py calls Google Places API in order to search locations, which is a paid service with a limited trial. 
  offlinetest.py uses existing cached data from Places API to conserve API keys for demonstrations. The data from the initial onlinetest.py run that was cached is available to see in onlinecache.txt.
  
  populartimes is a required dependency, so run `pip install pathto/populartimes-master` in cmd
  
  If you would like to use the live demonstration, first get a Google Maps API key https://developers.google.com/places/web-service/get-api-key. Next, paste it into `APIKey` in `onlinetest.py`. Finally, verify you have enabled Places API under Google's API Marketplace. 
  
  As of May 31, 2020, Google gives a free trial and will not charge the provided credit card without email verification once your free trial has concluded. 
 
