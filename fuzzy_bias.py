from fuzzywuzzy import fuzz   #fuzzywuzzy is a Python-based library that incorporates various Fuzzy logic functions
import data_set                # import dataset python file


#this function calculates the success ratio of our conversion algorithm

def conversion_success_rate(data_set):    # data_set is the list which contains all the data set in the form of tuples
	for e in data_set:
		english_to_hindi = kirans_function(e[0])      #converting each english text to hindi using kiran's function

		success_percentage = fuzz.ratio(english_to_hindi, e[1])    #compares the two text and returns the success rate

		return success_percentage


def partial_ratio_rate(data_set):
	for e in data_set:
		english_to_hindi = kirans_function(e[0])
		partial_ratio_percentage = fuzz.partial_ratio(english_to_hindi, e[1])

		return partial_ratio_percentage        #prints the partial ratio % between the two input text


#Returns 'Match!' if the conversion success rate is 100%

def print_ans(data_set):
	for e in data_set:
		english_to_hindi = kirans_function(e[0])
		
		if not [word for word in english_to_hindi.split(' ') if word not in e[1].split(' ')]:
    		print 'Match found!'             
