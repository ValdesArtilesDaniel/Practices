#Daniel Valdés Artiles // 26-01-2024 

from math import sqrt #import function math that will be useful later

#First Step: create a function that creates a dictionary using the txt data,
#with the index and the data related with the index, adn return this dictionary
#a variable 

def dictionaryGenerator(file):
    dictionary = {} #initialize with a void dictionary
    with open(file, 'r') as file: 
        for line in file: #read each line of the txt data saved in variable file_name 
            index, word = line.strip().split(' ', 1) #separates the index and the word
            dictionary[int(index)] = word #save the values of in the dictionary
    return dictionary

#Second Step: create a function with a dictionary input, this function
#will check what is the max index in the dictionary,
#and next to this will calculate how many rows will have the pyramid

def max_index(dictionary):
    maxIndex = 0 #initialize the maxIndex in 0
    for i in dictionary: 
        if i > maxIndex: #search for the largest index in the dictionary
            maxIndex = i    
    n = (-1+sqrt(1+8*maxIndex))/2 #calculate the number of rows for the pyramid using the largest index
    return n

#Third Step: create a function with a maxRows and dictionary input.
#this function will iterate in the dictionary searching for the data related
#with the index in maIndexperRow that is the max index in each row of the colum,
#and when the data is founded concat this data into a variable String with a " " 
#between each word, and return the full sentence.

def inMaxIndex(maxRows, dictionary):
    n = 1 #initialize n
    String = "" #set String in void by default 
    while n <= maxRows: 
        maxIndexperRow = (n*(n+1))/2 #search the data content in the last index for each floor of the pyramid
        String = String + dictionary[maxIndexperRow] + " " #concat the data in one string 
        n = n+1 #change to the next pyramid floor
    return String

#From this lines onwards is code to call functions bellow
file_name = 'coding_qual_input.txt' #create a variable with the txt information
myDictionary = dictionaryGenerator(file_name) #create the dictionary with DictionaryGenerator function
numberofRows = max_index(myDictionary) #calculate the max number of rows 
FinalString = inMaxIndex(numberofRows, myDictionary) #takes the final sentence decoded
print(FinalString)

