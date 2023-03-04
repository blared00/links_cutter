import random

from db_apps.cutter import schemas


async def check_link(link: str):
    return True


async def creating_link(link: str):
    chars_list = list(link.replace(':', '').replace('/', '').replace('.', ''))
    random.shuffle(chars_list)
    return ''.join(chars_list[5:10])


async def insert_link(link: str, new_link: str):
    return


async def remove_link(link_obj: schemas.Link):
    return


async def find_short_link(link: str):
    return


async def find_full_link(link: str):
    return
