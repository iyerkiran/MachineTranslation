# coding=utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from flask import Flask
import azure_translate_api
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello():
    name=request.form['inputtext']
    print name
    client = azure_translate_api.MicrosoftTranslatorClient('machinetranslationmanishrana','mjbYdQ3SyROItdT1gJAXUcIxYlBDaEKs3oKZ8XcFq0w=') # replace the client secret with the client secret for you app.
    translated = client.TranslateText(name, 'en', 'hi')
    print translated
    translated = translated.replace('"',"")
    return render_template('index.html', name=name, translated=translated)


if __name__ == '__main__':
    app.run(debug=True)