# Fly on rails
This repository contains a project named "Fly on rails" can help users of creating a trip around Ukraine. 
Choose the main city, where you want to start your journey and ctart a trip. I`d rather called it expedition, because during this routes
you will feel all the beauty of Ukraine regions and regions centers. 

# Input data:
1 - place you want to start the journey

2 - names of regions you want to visit more

# Output:
Main route - that consists of all routes together.
You will get - all departure times and arrival times, train numbers and travel time

# Project structure
Project has a **httplib2** folder which consists of 1 main program --->  **route_maker**  <---- that you need to run. 
Other folders contains helping classes and functions

- input 

    Functions -- get_input -- and -- check_input -- initial processing of inputed data.

- prosessing_API_funcs 

    contains functions that works mainly with UZ API from https://booking.uz.gov.ua , searches the most quick route between two cities or 
    stations. Returns the second part of global information

- return_class
  
    Folder contains classes for output representation - Return and RouteInfo ADT.

- stations_data 
  
    Main folder with StationArray and Station ADT. Gets stations, creates region routes and main routes, calls Return and CurTime classes for 
    further prosessing.

- time_data

  consists of the only class, representing time and data. 

# Instructions
- While running route_maker.py you will face a question:
    "Enter your city: (Львів, Київ, Харків, Одеса, Запоріжжя)
                       (Lviv, Kyiv, Kharkiv, Odessa, Zaporizzia)"
  
    You need to enter one of the cities:
      lviv or odessa or kyiv or kharkiv or zaporizzia
- Then you can enter sity by sity
    Example:
    Львів or Lviv
    Запоріжжя or Zaporizzia
    Одеса or Odessa 
   To end the list, just press **ENTER**
 
 
