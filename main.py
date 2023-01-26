import asyncio

import httpx as httpx

url = "http://192.168.70.119:3005/component/socparser/authorization/login"


async def req():
    async with httpx.AsyncClient() as session:
        payload = {
            "login": "java_api",
            "password": "4yEcwVnjEH7D"
        }
        res = await session.post(url, json=payload)
        print(f"async {res.headers}")


if __name__ == '__main__':
    import requests
    import json


    payload = json.dumps({
        "login": "java_api",
        "password": "4yEcwVnjEH7D"
    })
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"requests {response.headers}")
    loop = asyncio.get_event_loop()
    coroutine = req()
    loop.run_until_complete(coroutine)


