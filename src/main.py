from aiohttp import web
import os


async def handle(request):
    name = request.match_info.get('name', 'World')
    text = f"Hello, {name}!"
    return web.Response(text=text)


async def health_check(request):
    return web.json_response({"status": "healthy", "message": "Server is running"})


async def home(request):
    return web.Response(text="Welcome to my aiohttp server!")


def create_app():
    res = web.Application()
    res.router.add_get('/', home)
    res.router.add_get('/health', health_check)
    res.router.add_get('/{name}', handle)
    return res


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 8080))
    web.run_app(
        app,
        port=port,
        host='0.0.0.0'
    )