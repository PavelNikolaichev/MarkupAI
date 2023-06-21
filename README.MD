# About this project
MarkupAI(naming is awful :disappointed:) is a web app that is marking the spots/areas on the map from the ordinary text. Ofc, we are using NLP techniques as well as API of other map software.

# Installation
Just run: `pip install -r requirements.txt`.

Then, if this is your first run, you should apply migrations: `python manage.py migrate`.

# Usage
WARNING: if you want to use this app in production environment, you should change your `SECRET_KEY` var in `settings.py`.
You could generate it by using `get_random_secret_key()` function from `django.core.management.utils`.

Just run django server: `python manage.py runserver < ip:port(optional) >`

# TODO:
- [x] Implement a model.
- [x] Implement a web-app to pass down the text into the model.
- [x] Connect to `Yandex`/`<map_name>` API to make the marks.
- [ ] **(OPTIONAL)** Make a model implementation from scratch.
- [ ] **(OPTIONAL)** Dockerize this app.