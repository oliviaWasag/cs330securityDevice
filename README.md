# cs330securityDevice
It is a security device that goes through a string of numbers searching for the unlock and lock code. I built it by first creating my function with a name for the list of integers that will be read through, I named it password. I then assiged my unlock and lock codes and then creating a for loop with a few if statements inside. The for loop is designed to be executed when it is in the range of the list of integers(password). The if statements were designed to be read through every 6 digits and then if its not in those 6 then I would increment by +1 to read the next 6. If found and it matches my unlock code then it will unlock, if found and it matches my lock code it locks. 

For the second part I created a while loop to keep looping through until it breaks, using a series of if statements within this loop I am checking for if it matches my unlock code then it will unlock, if found and it matches my lock code it locks. I also have a counter running to see how many symbols it passes through until it is able to break. 
My code is written in python and it is written by me

You can test my code by inputing your own string of integers and seeing if it unlocks and locks the security device. 
I also created unittesting methods to see if the code passes as well.
