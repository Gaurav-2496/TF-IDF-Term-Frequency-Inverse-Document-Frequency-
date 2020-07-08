

'''Description : The following program will consist of choice function which will calculate the TF-IDF for the given
term and returns which document is most suitable  '''


import pandas as pd                           #import pandas for creating dataframe
import preprocessor
import word
import idf

#this function calculate the TF-IDF for the given term and returns which document is most suitable  '''
def choice(term,documents):
     dict={}                          #creating a empty dictionary
     tf = documents.data[term]        #extracting term frequency value of a given term using document object
     idf = documents.getIDF(term)     #calculating IDF by calling getIDF method from IDFAnalyser class
     for value in tf:                 #for loop to calulate TF-IDF
          tf_idf = value * idf        #calculating TF-IDF by multiplying idf to idf of term in each document
          dict[tf_idf]=term           #displaying data in dictionary format
     #creating dataframe
     final=pd.DataFrame(list(dict.items()),columns=['tf_idf','term'],index=documents.data.index)
     high=final['tf_idf'].idxmax()    #retrieves the maximum value in the dataframe with column name as tf_idf
     print("word :" + str(term)+"\n" + "tf-idf  :"+ str(high))
     return high                       #returns the highest TF-IDF score for the query term





p = preprocessor.Preprocessor()
cleaned_book=p.read_text('11-0.txt')
cleaned=p.clean()
w=word.WordAnalyser()
analyse_words=w.analyse_words(cleaned)
print(analyse_words)
frequency=w.get_word_frequency()
id=idf.IDFAnalyser()
a1=id.load_frequency(frequency,cleaned)
idf_value=id.getIDF("project")
print("The Idf value of the term you specified is",idf_value)
choice("project",id)








