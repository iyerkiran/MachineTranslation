import azure_translate_api

client = azure_translate_api.MicrosoftTranslatorClient('machinetranslationmanishrana',  # make sure to replace client_id with your client id
                                                       'mjbYdQ3SyROItdT1gJAXUcIxYlBDaEKs3oKZ8XcFq0w=') # replace the client secret with the client secret for you app.
print client.TranslateText('God is great', 'en', 'hi')