import asyncio
import aiohttp
import random

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            sleep_interval = random.uniform(1, 5)
            await asyncio.sleep(sleep_interval)
            content = await response.json()
            return content

async def main():
    urls = ['https://pokeapi.co/api/v2/pokemon/1','https://pokeapi.co/api/v2/pokemon/2','https://pokeapi.co/api/v2/pokemon/3']
    tasks = [fetch_url(url) for url in urls]
    result = await asyncio.gather(*tasks)

    for x,data in enumerate(result):
        #print(f"Id{data['id']}")
        print(f"Name: {data['name']}")
        print(f"Height: {data['height']}")
        
asyncio.run(main())
