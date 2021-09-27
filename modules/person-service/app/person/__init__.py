from app.person.models import Person 
from app.person.schemas import PersonSchema 

def register_routes(api, app, root="api"):
    from app.person.controllers import api as person_api

    api.add_namespace(person_api, path=f"/{root}")
