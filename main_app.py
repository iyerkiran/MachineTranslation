# coding=utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from flask import Flask
import support_library
from flask import Flask, render_template, request, make_response
#import nltk 
#import langid
import mtranslate
from googletrans import Translator
from Data_set import data_set
app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello():
    translator = Translator()
    input_src=request.form['inputtext']
    print input_src
    #b=mtranslate.translate(name,"hi","utf8")
    #b=b.encode('utf-8')
    #print b.encode("utf-8")
    
    detected = translator.detect(input_src)

    if detected.lang == "hi":
        input_detected = "Hindi"
        output_detected = "English"
        destination_code = "en"
    if detected.lang == "en":
        input_detected = "English"
        output_detected = "Hindi"
        destination_code = "hi"
     
    output_src = translator.translate(input_src, src=detected.lang, dest=destination_code)    
    print output_src.text
    #connect to the microsoft cloud for searching the various corpora of the english language with their corrosponding hindi corpora.
    #tokens = tokens = nltk.word_tokenize(name)
    #print tokens
    #pos_tagging = nltk.pos_tag(tokens)
    #print pos_tagging
    #client = support_library.MicrosoftTranslatorClient('machinetranslationmanishrana','mjbYdQ3SyROItdT1gJAXUcIxYlBDaEKs3oKZ8XcFq0w=')
    #language = langid.classify(name)
    '''if language[0] == 'en':    
        translated = client.TranslateText(name, 'en', 'hi')
        input_detected = "English"
        output_detected = "Hindi"
        translated = translated.replace('"',"")
        data_set.append((name, translated))
    else:
        translated = client.TranslateText(name, 'hi', 'en')
        input_detected = "Hindi"
        output_detected = "English"
        translated = translated.replace('"',"")
        data_set.append((translated, name))'''
    #output_detected="tst"
    #translated=name
    #input_detected="test"
    return render_template('index.html', name=input_src, translated=output_src.text, input_detected=input_detected,output_detected=output_detected)
    

if __name__ == '__main__':
    app.run(debug=True) #this ensures auto reloading of the server on detecting any change in the backend.