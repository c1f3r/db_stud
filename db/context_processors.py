from db_stud import settings

def settings_context(request):
    return {'settings': settings}