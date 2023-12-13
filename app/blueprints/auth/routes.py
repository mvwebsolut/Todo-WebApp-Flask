from . import blueprint

@blueprint.route('/')
def home_auth():
    return "Home Auth"