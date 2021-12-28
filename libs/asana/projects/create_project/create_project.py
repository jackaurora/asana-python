from aiohttp import web
import json
import asana
from utils.parse_config import *


f = open('./libs/asana/projects/create_project/data.json')

# returns JSON object as
# a dictionary
body = json.load(f)


async def create_a_project(request):
    print("Create a project on a task")
    oauth = parse_config()['ASANA']['personal_access_token']
    print("oath", oauth)
    #work_id = request.query['work_id']
    #body = request.query['body']
    id = '1201396020093243'

    try:
        client = asana.Client.access_token(oauth)

        result = client.projects.create_project(
            {'workspace': id, 'body': body}, opt_pretty=True)

        response_obj = {'message': "Create a project successfully",
                        'results': result, }
        return web.Response(text=json.dumps(response_obj))
    except Exception as err_parse:
        response_obj = {'message': "Create a project failed",
                        'error_type': str(err_parse)}
        return web.Response(text=json.dumps(response_obj))


# app = web.Application()
# app.router.add_get('/', create_a_story_on_a_task)
#
# web.run_app(app)
