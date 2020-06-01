# IOhackHackathon2020 (PopQ!)
  PopQ! by BLACKPINK

  PopQ!, or popular times and queue, is an all-in-one webpage designed for facilitating social distancing by directing users to less busy stores as well as providing a remote queue system so that users may stay in their cars while waiting for busy services.

**If you have access to our pitch video, please go to dependencies.txt, read it, and download the dependencies. Then, read how to run below and Queue**

# How to run
  Please note that without access to the Google API, it is not possible to update the suggested places. The places that the offline version (offlinetest.py) currently return are taken from a set list called onlinecache.txt. However, onlinetest.py will be a dropin replacement for offlinetest.py and will actually use the Google API. It will therefore take an input of a store and return stores that have the lowest current popularity within a 5km radius, provided you have an API key. The logic for the online Google API has already been coded in, but the usage of an API key poses certain financial costs. Thus, for the sake of this project, we are using the offline version as a proof of concept.
  
  To run the entire project as whole, cd to the directory IOhackHackathon2020 (or wherever you cloned it), and run node app.js. Then, to view the website, go to "localhost:5000" on a web browser (preferably google chrome).

  Please see the video for a much more detailed explanation of how to run the code.
# pt (populartimes)
  The goal of this program is to give users advice in order to avoid crowds at stores and public places. 
  From a user provided store and radius, PopQ! searches the area for similar stores that have the lowest live volume using Google's    popular times API. 
  
  onlinetest.py calls Google Places API in order to search locations, which is a paid service with a limited trial. 
  offlinetest.py uses existing cached data from Places API to conserve API keys for demonstrations. The data from the initial onlinetest.py run that was cached is available to see in onlinecache.txt. No user input is needed, it simply sorts the information provided. 
  
  populartimes is a required dependency, so run `pip install pathto/populartimes-master` in cmd
  
  If you would like to use the live demonstration, first get a Google Maps API key https://developers.google.com/places/web-service/get-api-key. Next, paste it into `APIKey` in `onlinetest.py`. Finally, verify you have enabled Places API under Google's API Marketplace. 
  
  As of May 31, 2020, Google gives a free trial and will not charge the provided credit card without email verification once your free trial has concluded. 
 
 # Queue
 The purpose of our queueing is to let users stay outside while keeping their place in line. The queue system takes a user login using an email and a password, and if the user does not have an account, they are redirected to a signup page. 

 # Business End
 Businesses also have a convenient platform to register with PopQ. By filling out the online form and logging in (the template pages for login and registration are shown in businesss_signin.html and business_signup.html), businesses are able to easily integrate themselves into the backend servers of PopQ. The python script, "new_company.py", automatically creates a series of databases and backend framework for a business when they register with a given ID. Thus, by combining easy user access and efficient business registration, we were effectively able to create a platform to link different groups of people together, making shopping safer and better than ever.

 # Dependencies
node js
	express
	socket.io
python
	populartimes
	time
	sys

 # Project status and TODO
 Currently, the project is an excellent proof of concept that features all of the necessary functions for what it is supposed to be. In the future, we plan on increasing the robustness of the web application, increasing security and reducing the frequency of rare bugs when they occur.

