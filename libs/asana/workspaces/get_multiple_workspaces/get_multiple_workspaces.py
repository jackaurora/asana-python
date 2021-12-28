from aiohttp import web
import json
import asana
from utils.parse_config import *


async def get_multiple_workspaces(request):
    # No GID Required
    # No Body Parameters
    # Optional Paramaters:
    # ?opt_pretty boolean	Provides “pretty” output.
    # ?opt_fields array[string]	Defines fields to return.
    # ?limit integer	Results per page.
    # ?offset string	Offset token.

    oauth = parse_config()['ASANA']['personal_access_token']
    print("oath", oauth)
    body = {}

    try:
        client = asana.Client.access_token(oauth)
        result = list(client.workspaces.get_workspaces(opt_pretty=True))
        response_obj = {'message': "Get Asana Workspaces Success",
                        'results': result, }
        return web.Response(text=json.dumps(response_obj))
        # return web.Response(text=json.dumps(list(result)))
        # So on a fetch here, a json response can be received
        # This can then be handled on the front-end

    except Exception as err_parse:
        response_obj = {'message': "Get Asana Workspaces Failed",
                        'error_type': str(err_parse)}
        return web.Response(text=json.dumps(response_obj))