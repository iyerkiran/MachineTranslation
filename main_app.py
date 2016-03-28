# coding=utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from flask import Flask
import support_library
from flask import Flask, render_template, request, make_response
import nltk 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello():
    name=request.form['inputtext']
    #connect to the microsoft cloud for searching the various corpora of the english language with their corrosponding hindi corpora.
    tokens = tokens = nltk.word_tokenize(name)
    print tokens
    pos_tagging = nltk.pos_tag(tokens)
    print pos_tagging
    quit()
    client = support_library.MicrosoftTranslatorClient('machinetranslationmanishrana','mjbYdQ3SyROItdT1gJAXUcIxYlBDaEKs3oKZ8XcFq0w=')
    translated = client.TranslateText(name, 'en', 'hi')
    translated = translated.replace('"',"")
    return render_template('index.html', name=name, translated=translated)


if __name__ == '__main__':
    app.run(debug=True) #this ensures auto reloading of the server on detecting any change in the backend.