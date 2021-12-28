from aiohttp import web
import json
import asana
from utils.parse_config import *


async def delete_a_project(request):
    # No GID Required
    # No Body Parameters
    # Optional Paramaters:
    # ?opt_pretty boolean	Provides “pretty” output.
    # ?opt_fields array[string]	Defines fields to return.
    # ?limit integer	Results per page.
    # ?offset string	Offset token.

    oauth = parse_config()['ASANA']['personal_access_token']
    print("oath", oauth)
    # project_gid = request.query['gid']
    project_gid = '1201463049482251'
    try:
        client = asana.Client.access_token(oauth)
        result = client.projects.delete_project(
            project_gid, opt_pretty=True)
        response_obj = {'message': "delete Asana project Success",
                        'results': result, }
        return web.Response(text=json.dumps(response_obj))
        # return web.Response(text=json.dumps(list(result)))
        # So on a fetch here, a json response can be received
        # This can then be handled on the front-end

    except Exception as err_parse:
        response_obj = {'message': "delete Asana project Failed",
                        'error_type': str(err_parse)}
        return web.Response(text=json.dumps(response_obj))
