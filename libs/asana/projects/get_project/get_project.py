from aiohttp import web
import json
import asana
from utils.parse_config import *


async def get_a_project(request):
    # No GID Required
    # No Body Parameters
    # Optional Paramaters:
    # ?opt_pretty boolean	Provides “pretty” output.
    # ?opt_fields array[string]	Defines fields to return.
    # ?limit integer	Results per page.
    # ?offset string	Offset token.

    oauth = parse_config()['ASANA']['personal_access_token']
    print("oath", oauth)
    #workspace_id = request.query['workspace_id']
    # body = request.query['body']
    #project_id = request.query['project_id']
    id = '1201396020093243'
    body = {}
    project_id = '1201463049482251'

    try:
        client = asana.Client.access_token(oauth)
        result = client.projects.get_project(
            project_id, {'workspace': id, 'body': body}, opt_pretty=True)
        response_obj = {'message': "Get Asana project Success",
                        'results': result, }
        return web.Response(text=json.dumps(response_obj))
        # return web.Response(text=json.dumps(list(result)))
        # So on a fetch here, a json response can be received
        # This can then be handled on the front-end

    except Exception as err_parse:
        response_obj = {'message': "Get Asana project Failed",
                        'error_type': str(err_parse)}
        return web.Response(text=json.dumps(response_obj))
