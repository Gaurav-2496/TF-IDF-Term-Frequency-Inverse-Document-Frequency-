

'''Description : The following program will create class to display frequency of words into dataframe and calculate
the idf of each word'''
'''IDF stands for Inverse Document Frequency, it is a staistic that attempt to categorize how important a term is 
 within the corpus of documents'''

import pandas as pd  #importing pandas for dataframe
import math          #importing math class for calculating IDF
import preprocessor
import word


class IDFAnalyser:

# constructor for creating instance variable
  def __init__(self):
      self.data = pd.DataFrame()   #Defining instance variable data to hold the DataFrame


#this method loads the frequency of cleaned data into data with title corresponding to text frequency was generated
  def load_frequency(self,book_frequency,book_title):

 #creates the dataframe and stores the frequency of book with title in the dataframe variable
      dataframe = pd.DataFrame(book_frequency,index=[book_title])
      self.data = self.data.append(dataframe,sort=True)      #appends the dataframe variable to self.data
      return self.data                                       #returns dataframe into self.data



#this method obtains the IDF for the term provided and the documents loaded into the data
  def getIDF(self,term):
      num_of_docs=len(self.data.index)                  #stores the number of Documents present in dataframe
      count=self.data[term].count()                     #stores the count of number of documents containing the term
      calc_idf = 1 + math.log(num_of_docs / 1 + count)  #calculate the IDF and stores in calc_idf variable
      return calc_idf                                   #returns calc_idf variable



p = preprocessor.Preprocessor()
cleaned_book=p.read_text('11-0.txt')
cleaned=p.clean()
w=word.WordAnalyser()
analyse_words=w.analyse_words(cleaned)

frequency=w.get_word_frequency()

i=IDFAnalyser()
i.load_frequency(frequency,cleaned)

idf_value=i.getIDF("web")
print("The Idf value of the term you specified is",idf_value)






