from aiohttp import web
import json
import asana
from utils.parse_config import *


async def create_a_story_on_a_task(request):
    print("Create a story on a task")
    oauth = parse_config()['ASANA']['personal_access_token']
    print("oath", oauth)
    task_gid = request.query['task_gid']
    body = request.query['body']

    try:
        client = asana.Client.access_token(oauth)
        body = json.loads(body)
        result = client.stories.create_story_for_task(
            task_gid, body, opt_pretty=True)

        response_obj = {'message': "Create story successfully",
                        'results': result, }
        return web.Response(text=json.dumps(response_obj))
    except Exception as err_parse:
        response_obj = {'message': "Create story failed",
                        'error_type': str(err_parse)}
        return web.Response(text=json.dumps(response_obj))


# app = web.Application()
# app.router.add_get('/', create_a_story_on_a_task)
#
# web.run_app(app)
