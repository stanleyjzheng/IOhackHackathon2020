![PopQLogo](https://img.techpowerup.org/200601/popq.png)

# PopQ!
PopQ!, or popular times and queue, is an all-in-one webpage designed for facilitating social distancing by directing users to less busy stores as well as providing a remote queue system so that users may stay in their cars while waiting for busy services.

## Getting Started

### Install dependencies
* [node.js](https://nodejs.org/en/)
* [populartimes](https://github.com/m-wrzr/populartimes)

Using the links above, install node.js and populartimes to your computer.

Navigate to the directory and then use the package manager pip to install populartimes.
```
pip install pathto/populartimes-master
```
### Get API Key (optional)

If you would like to use the live demonstration, first get a [Google Maps API key](https://developers.google.com/places/web-service/get-api-key). Next, paste it into `APIKey` in `onlinetest.py`. Finally, verify you have enabled Places API under Google's API Marketplace. 

`onlinetest.py` calls Google Places API in order to search locations, which is a paid service with a limited trial. 

`offlinetest.py` uses existing cached data from Places API to conserve API keys for demonstrations. The data from the initial `onlinetest.py` run that was cached is available to see in `onlinecache.txt`. No user input is needed, it simply sorts the information provided. 

The places that the offline version currently returns are taken from a set list called `onlinecache.txt`. However, `onlinetest.py` is a drop in replacement for `offlinetest.py` and will use the Google API, and will therefore take an input of a store and return stores that have the lowest current popularity within a 5km radius, provided you have an API key.

As of May 31, 2020, Google gives a free trial and will not charge the provided credit card without email verification once your free trial has concluded.

### How to run
  Please note that without access to the Google API, it is not possible to update the suggested places. The places that the offline version (offlinetest.py) currently return are taken from a set list called onlinecache.txt. However, onlinetest.py will be a dropin replacement for offlinetest.py and will actually use the Google API. It will therefore take an input of a store and return stores that have the lowest current popularity within a 5km radius, provided you have an API key. The logic for the online Google API has already been coded in, but the usage of an API key poses certain financial costs. Thus, for the sake of this project, we are using the offline version as a proof of concept.
  
  To run the entire project as whole, cd to the directory IOhackHackathon2020 (or wherever you cloned it), and run node app.js. Then, to view the website, go to "localhost:5000" on a web browser (preferably google chrome).

  Please [see our video](https://drive.google.com/file/d/1T_EUTfL4Vxr-2CFCptyMnkComfYJYBSz/view?usp=sharing) for a much more detailed explanation of how to run the code.

## Features

### Popular Times

The goal of this program is to give users advice in order to avoid crowds at stores and public places. 
From a user provided store and radius, PopQ! searches the area for similar stores that have the lowest live volume using Google's    popular times API. 

 ### Queue
 The purpose of our queueing is to let users stay outside while keeping their place in line. The queue system takes a user login using an email and a password, and if the user does not have an account, they are redirected to a signup page. 

### Business End
 Businesses also have a convenient platform to register with PopQ. By filling out the online form and logging in (the template pages for login and registration are shown in businesss_signin.html and business_signup.html), businesses are able to easily integrate themselves into the backend servers of PopQ. The python script, "new_company.py", automatically creates a series of databases and backend framework for a business when they register with a given ID. Thus, by combining easy user access and efficient business registration, we were effectively able to create a platform to link different groups of people together, making shopping safer and better than ever.

## Built With
* [node.js](https://nodejs.org/en/) - The runtime environment used
* [socket.io](https://www.npmjs.com/package/socket.io) - Used to actively communicate between front and back end
* [express](https://expressjs.com/) - Used to handle HTTP requests
* [populartimes](https://github.com/m-wrzr/populartimes) - Used to find popular times data
* [qrcodejs](Davidshimjs.github.io/qrcodejs/) - QR code generator

## Authors
* **Richard Zhang** - [Rougg](https://github.com/Rougg)
* **Michael Xu** - [themicklepickle](https://github.com/themicklepickle)
* **Benjamin Ng** - [bennnyhin](https://github.com/bennnyhin)
* **Stanley Zheng** - [Stanley-Zheng](https://github.com/Stanley-Zheng)
* **Andy Zhou** - [VexusDoom](https://github.com/VexusDoom)
