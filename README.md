# Narrate with Images
This is a django app which gives the images related to the text given and also pronounce it. A bi-lstm+crf named entity recognition model is trained on Connel 2003 dataset to give the entities in the text which are searched in google to get relevant images. For speech generation tacotron model is used.

Python version tested: 3.6<br>
Steps:
1) Create and activate virtualenvironment with python 3
2) pip install -r requirements.txt
3) Add a glove vector file(50d6Bwords) to run the model.
4) python manage.py makemigrations narration
5) python manage.py migrate
6) python manage.py runserver

Open localhost:8000 
The audio file will be stored in narration/saved_audio as {title_mentioned_in_form}.wav and the images will be shohwn related to the text
