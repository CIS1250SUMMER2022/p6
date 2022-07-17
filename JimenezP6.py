# JimenezP6
# Programmer: Mark Jimenez
# Email: mjimenez43@cnm.edu
# Purpose: Demonstrate use of functions

import math



def header():
	print("Hello, this is a program to help determine the geographical distance between two points anywhere in the world")
	print("---------------------------------------------------------------------------------------------------------------")
	
def get_location():
	latitude1 = float(input("Please enter the latitude of the first location: ")) * (math.pi/180)
	longitude1 = float(input("Please enter the longitude of the first location: ")) * (math.pi/180)
	latitude2 = float(input("Please enter the latitude of the second location: ")) * (math.pi/180)
	longitude2 = float(input("Please enter the longitude of the second location: ")) * (math.pi/180)
	global locationList
	locationList = [latitude1, longitude1, latitude2, longitude2]
	return locationList
	
def distance(location):

	R = 6371
	
	A = (math.sin((location[0] - location[2])/2))**2 + math.cos(location[0]) * math.cos(location[2]) * (math.sin((location[1] - location[3]/2)))**2
	C = 2 * math.atan2(math.sqrt(A),math.sqrt(1-A))
	D = R * C
	return D
	

choice = "y"
while (choice == "y"):
	header()
	get_location()
	distance = distance(locationList)
	print(f"The distance between those two points is {distance} kilometers.")
	
	choice = input("Do you want to find the distance between two other locations? (y/n): ")
	
print("Goodbye!")
