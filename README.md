# cs330securityDevice
It is a security device that goes through a string of numbers searching for the unlock and lock code. I created a function that will go through the string using the FSM. It checks if the single interger matches the code and if it does it moves up in states if not it moves back down. Then at the end it goes off to 2 different states unlock and lock state 
For the second part I created a while loop to keep looping through until it breaks. I reused my function from part 1 and added on a seperate function that will scan if it unlocks and then records the time it took and how many characters were passed when it was needed to break.
My code is written in python and it is written by me

You can test my code by running the unittesting I provided for the code.

 MY MEMO BELOW:
 Security Device Project 

My project was able to take in a list of  a string of numbers, and scan it to see if any of the 6 consecutive numbers matched either my unlock or lock code. By using the Finite State machine I had a method that would take each individual digit and see if it was the right digit needed to continue on to the next state. If it made it to my final states it was able to lock or unlock the code.I had the same path for part two but I had to put in a random string of unknown length instead.

My findings from this project show that my first part runs very efficiently, My unit test cases all pass without errors. My second part on the other hand depends on the random string. My quickest time was .5 seconds and it went through 500+ characters to find the password. But since it is random and searching for a specific 6 digit code it can take upwards of an hour to pass as well with it passing through hundreds of thousands of characters. 

My Finite Automata is written by going through the digits in a straight line and if I were to run into an 8, that is the first digit in my code it would get sent back to state 1, and if it wasn't the number needed or an 8 it would get sent back all the way to the start, state 0.
The average of my recorded times for part 2 were 438 seconds. I would stop and rerun the test cases if they took longer than 15 minutes. 

[fsm 330.docx](https://github.com/oliviaWasag/cs330securityDevice/files/10070766/fsm.330.docx)
^ my FSM diagram designed from Graphviz Visual Editor
