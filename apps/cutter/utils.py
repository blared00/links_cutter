import random

import aiohttp
from decouple import config

from db_apps.cutter import schemas
from db_apps.cutter.async_crud import create_link, get_short_link_by_full, get_full_link_by_short, delete_link


async def check_link(link: str):
    timeout = aiohttp.ClientTimeout(total=int(config('TIMEOUT_REQUESTS', 5)))
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.head(link) as response:
                return 'success' if response.status < 400 else f'Response status {response.status}'
        except TimeoutError:
            return 'I guess problem with page loading'
        except (aiohttp.client_exceptions.InvalidURL,  aiohttp.client_exceptions.ClientConnectorError):
            return 'I guess your URL is invalid'


async def creating_link(link: str):
    chars_list = list(link.replace(':', '').replace('/', '').replace('.', ''))
    random.shuffle(chars_list)
    return ''.join(chars_list[5:10])


async def insert_link(link: str, new_link: str):
    link_obj = schemas.LinkCreate(
        short_link=new_link,
        full_link=link
    )
    await create_link(link_obj)
    return


async def remove_link(link_obj: schemas.Link):
    return await delete_link(link_obj)


async def find_short_link(link: str):
    return await get_short_link_by_full(link)


async def find_full_link(link: str):
    return await get_full_link_by_short(link)
