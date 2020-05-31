# IOhackHackathon2020
  2020 I/OHack Pandemic Hackathon project by team BLACKPINK


**pt (populartimes)**
  
  From a user provided store and radius, we search the area for similar stores that have lower current volume using Google's popular times API. 
  
  onlinetest.py calls Google Places API about 3000 times per run (out of 12000) of a free trial in order to search locations. 
  offlinetest.py uses existing cached data from Places API so that we conserve API keys. The data from the initial onlinetest.py run that was cached is available to see in onlinecache.txt.
  
  populartimes is a required dependency, so run `pip install pathto/populartimes-master` in cmd
