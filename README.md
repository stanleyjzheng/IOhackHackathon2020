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

If you would like to use the live demonstration, first get a Google Maps API key https://developers.google.com/places/web-service/get-api-key. Next, paste it into `APIKey` in `onlinetest.py`. Finally, verify you have enabled Places API under Google's API Marketplace. 

onlinetest.py calls Google Places API in order to search locations, which is a paid service with a limited trial. 

offlinetest.py uses existing cached data from Places API to conserve API keys for demonstrations. The data from the initial `onlinetest.py` run that was cached is available to see in `onlinecache.txt`. No user input is needed, it simply sorts the information provided. 

The places that the offline version currently returns are taken from a set list called `onlinecache.txt`. However, `onlinetest.py` is a drop in replacement for `offlinetest.py` and will use the Google API, and will therefore take an input of a store and return stores that have the lowest current popularity within a 5km radius, provided you have an API key.

As of May 31, 2020, Google gives a free trial and will not charge the provided credit card without email verification once your free trial has concluded.


## Features

### Popular Times

The goal of this program is to give users advice in order to avoid crowds at stores and public places. 
From a user provided store and radius, PopQ! searches the area for similar stores that have the lowest live volume using Google's    popular times API. 

 ### Queue
 The purpose of our queueing is to let users stay outside while keeping their place in line. The queue system takes a user login using an email and a password, and if the user does not have an account, they are redirected to a signup page. 

## Built With
* [node.js](https://nodejs.org/en/)
* [populartimes](https://github.com/m-wrzr/populartimes)

## Authors
* **Richard Zhang**
* **Michael Xu**
* **Benjamin Ng**
* **Stanley Zheng**
* **Andy Zhou**