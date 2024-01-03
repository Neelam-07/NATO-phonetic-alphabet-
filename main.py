# NATO phenotic alphabet

import pandas

data= pandas.read_csv("./nato project/nato_phonetic_alphabet.csv")
# print(data)

# use itterrow method to convert the csv data into dict using pandas and dict comph

phenotic_dict= {row.letter: row.code for (index, row) in data.iterrows()}
# print(phenotic_dict)

# get a list of phenotic alphabetes using list comp. : 

word= input("enter the word\n").upper()

phenotic_list= [phenotic_dict[letter] for letter in word]
print(phenotic_list)
