# cell-1
# Here are all the installs and imports you will need for your word cloud script and uploader widget

# Installs and imports

#!pip install wordcloud
#!pip install fileupload
#!pip install ipywidgets
#!jupyter nbextension install --py --user fileupload
#!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# cell-2
# This is the uploader widget
# This will ask you to upload a  text file, of which the wordcloud is going to be created
def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 ** 10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)


_upload()


# cell-3
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    file_contents2 = ""
    for index, char in enumerate(file_contents):
        if char.isalpha() == True or char.isspace():
            file_contents2 += char

    file_contents2 = file_contents2.split()
    file_without_words = []

    for word in file_contents2:
        if word.lower() not in uninteresting_words and word.isalpha() == True:
            file_without_words.append(word)

    frequencies = {}

    for word in file_without_words:
        if word.lower() not in frequencies:
            frequencies[word.lower()] = 1
        else:
            frequencies[word.lower()] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# cell-4
# this will create the wordcloud image
# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
