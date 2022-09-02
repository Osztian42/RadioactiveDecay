#This program asks the user to enter the name of an isotope and its half-life along with the initial amount and elapsed time
#The amount of isotope remaining is displayed as well as the initial mass of isotope required to ensure 5 g remain after 30 seconds
#The amount of isotope remaining is then plotted against time
#This program allows data from multiple isotopes to be entered

#Import maths functions
import math as mt
import numpy as np
import matplotlib.pyplot as plt

#Create list for the names of all the isotopes
isotope_names=[]

#Set up while loop until user stops entering more isotopes
isotope = 0
while isotope != "stop":

# Ask user to input the name of a particular isotope 
  isotope = input ("Please enter the name of a radioactive isotope or type stop to complete the program")
  
# Loop ended when user types stop
  if isotope == "stop":
    break
  
# Adds name of isotope to list of names of isotopes
  isotope_names.append (isotope)
  
# Ask user to input half-life of the isotope in seconds
  half_life = float (input("Enter its half-life in seconds"))
  
# Ask user for the initial amount of the isotope in grams
  amount = float (input ("Enter initial amount of the isotope in grams"))
  
# Ask user for the elapsed time in seconds
  time = int (input("Enter elapsed time in seconds"))

# Calculate the amount of isotope (in grams) remaining after the elapsed time
  P = (1/2**(time/half_life))*amount

# Display the amount of isotope remaining
  print ("Isotope remaining after", time, "seconds is", P, "grams")

# Calculate and display initial mass of isotope to ensure 5 grams remain after 30 seconds
  initial_mass = (2**(30/half_life))*5
  print ("An initial mass of the isotope of",initial_mass,"g is required to ensure 5 g is left after 30 seconds" )

# Create an array of independent variables
  time = (np.linspace (0,10,100))
  
# Create a second array showing the amount of isotope remaining against time
  x = time
  y = amount*np.exp(-mt.log(2)*(time/half_life))

  plt.plot (x,y)
  
if isotope == "stop":

#Plot quantity of isotope remaining versus time
    plt.title ("Radioactive decay of isotope versus time")
    plt.xlabel("Time/s")
    plt.ylabel("Mass/g")
    plt.show ()
   
#Print out a list of all isotopes studied
print ("The isotopes studied were", isotope_names)
