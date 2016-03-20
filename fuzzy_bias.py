from fuzzywuzzy import fuzz   #fuzzywuzzy is a Python-based library that incorporates various Fuzzy logic functions
import dataset                # import abhinav's Python file



#this function calculates the success ratio of our conversion algorithm

def conversion_success_rate(data_set):    # data_set is the list which contains all the data set in the forn of tuples
	for e in data_set:
		english_to_hindi = kirans_function(e[0])      #converting each english text to hindi using kiran's function

		success_percentage = fuzz.ratio(english_to_hindi, e[1])    #compares the two text and returns the success rate

		print success_percentage


def partial_ratio_rate(data_set):
	for e in data_set:
		english_to_hindi = kirans_function(e[0])
		partial_ratio_percentage = fuzz.partial_ratio(english_to_hindi, e[1])

		print partial_ratio_percentage        #prints the partial ratio % between the two input text


#Returns 'Match!' is the conversion success rate is 100%

def print_ans(data_set):
	for e in data_set:
		english_to_hindi = kirans_function(e[0])
		
		if not [word for word in english_to_hindi.split(' ') if word not in e[1].split(' ')]:
    		print 'Match found!'             
