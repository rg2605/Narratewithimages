# text2Narrate
Python version tested: 3.4<br>
Steps:
1) Create and activate virtualenvironment with python 3
2) pip install -r requirements.txt
3) python manage.py makemigrations narration
4) python manage.py migrate
5) python manage.py runserver

Open localhost:8000 
The audio file will be stored in narration/saved_audio as {title_mentioned_in_form}.wav
