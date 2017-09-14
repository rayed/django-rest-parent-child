
# Parent Child with Django REST Framework

Sample Django project to demonstrate parent/child REST API

## Setup

    cd apps
    pip install --upgrade -r ../requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser


## REST API End points

### Parent End Points:

    /api/question/                  (GET: list, POST: create)
    /api/question/{id}/             (GET: retrieve, POST: update, DELETE: delete)

### Child End Points

    /api/question/{question_id}/choice/     (GET: list, POST: create)
    /api/question/{question_id}/choice/{id} (GET: retrieve, POST: update, DELETE: delete)
