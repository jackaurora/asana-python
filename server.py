from aiohttp import web

import libs.asana.stories.create_story.create_story
import libs.asana.workspaces.get_multiple_workspaces.get_multiple_workspaces
import libs.asana.projects.create_project.create_project
import libs.asana.projects.get_multiple_projects.get_multiple_projects
import libs.asana.projects.get_project.get_project
import libs.asana.projects.delete_project.delete_project
import utils.enable_logging
import libs.test.handle
import libs.test.new_user


class Server(web.Application):

    def __init__(self):
        super().__init__()

        # Add our route with a wildcard method which accepts GET/POST/PUT etc...
        # Can also use web.get('/some_route', self.some_route) etc...
        self.add_routes([
            # Asana Routes
            web.route(method='*', path="/asana/stories/create_story",
                      handler=self.create_story),
            web.route(method='*',
                      path="/asana/workspaces/get_multiple_workspaces",
                      handler=self.get_multiple_workspaces),
            # asana projects
            web.route(method='*', path="/asana/projects/create_project",
                      handler=self.create_project),
            web.route(method='*', path="/asana/projects/get_multiple_projects",
                      handler=self.get_multiple_projects),
            web.route(method='*', path="/asana/projects/get_project",
                      handler=self.get_project),
            web.route(method='*', path="/asana/projects/delete_project",
                      handler=self.delete_project),
            # Test Routes
            web.route(method='*', path='/test_new_user',
                      handler=self.test_new_user),
            web.route(method='*', path='/example_route',
                      handler=self.example_route),
            web.route(method='*', path='/handle', handler=self.handle),
        ])

    # asana projects
    async def create_project(self, request: web.Request):
        # logger is used to create log files
        return await libs.asana.projects.create_project.create_project.create_a_project(request)

    async def get_multiple_projects(self, request: web.Request):
        # logger is used to create log files
        return await libs.asana.projects.get_multiple_projects.get_multiple_projects.get_multiple_projects(request)

    async def get_project(self, request: web.Request):
        # logger is used to create log files
        return await libs.asana.projects.get_project.get_project.get_a_project(request)

    async def delete_project(self, request: web.Request):
        # logger is used to create log files
        return await libs.asana.projects.delete_project.delete_project.delete_a_project(request)

    # asana story
    async def create_story(self, request: web.Request):
        # logger is used to create log files
        utils.enable_logging.enable_logging().info('Asana Request - Create Story')
        return await libs.asana.stories.create_story.create_story.create_a_story_on_a_task(request)

    async def get_multiple_workspaces(self, request: web.Request):
        # logger is used to create log files
        utils.enable_logging.enable_logging().info(
            'Asana Request - Get Multiple Workspaces')
        return await libs.asana.workspaces.get_multiple_workspaces.get_multiple_workspaces.get_multiple_workspaces(request)

    async def test_new_user(self, request: web.Request):
        # logger is user to create log files
        utils.enable_logging.enable_logging().info(
            'Received a request to test new user')
        return await libs.test.new_user.new_user(request)

    async def handle(self, request: web.Request):
        utils.enable_logging.enable_logging().info('Received a request to handle')
        return await libs.test.handle.handle()

    async def example_route(self, request: web.Request):
        utils.enable_logging.enable_logging().info(
            'Receive A Request to /example_route')
        # Read query string parameters as a dict...
        # print(request.query)

        # Read Headers as a dict...
        print(request.headers)

        # Can send a JSON response with the method below...
        # return web.json_response(data)

        # Otherwise you can send a response like below...
        # return web.Response(status=200)


app = Server()
# cors = aiohttp_cors.setup(app, defaults={
#     "*": aiohttp_cors.ResourceOptions(
#             allow_credentials=True,
#             expose_headers="*",
#             allow_headers="*",
#         )
# })
#
# # Add all resources to `CorsConfig`.
# resource = cors.add(app.router.add_resource("/test_new_user"))
# cors.add(resource.add_route("POST", app.test_new_user))

# Start the asynchronous server...
web.run_app(app, host='localhost', port=4074)
