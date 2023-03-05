from decouple import config
from fastapi import HTTPException, status, APIRouter, Request
from fastapi.responses import JSONResponse, Response

from . import models
from .utils import check_link, creating_link, insert_link, find_short_link, remove_link, find_full_link


router = APIRouter(
    prefix='/cutter',
    tags=['Cutter'],
)


@router.get('/cut/')
async def create_short_link(link: str, request: Request) -> models.Link:
    """
    Get cutting link</br></br>

    link: link which need to cut
    """
    if 'http' not in link:
        link = 'https://' + link
    if (mes := await check_link(link)) != 'success':
        raise HTTPException(
            status_code=400,
            detail='Bad link. Can you double check link and send again? ' + mes
        )

    referer = config('HTTP_PREFIX') + request.headers.get('host') + '/'
    if exist_link := await find_short_link(link):
        return models.Link(
                short_link=referer + exist_link.short_link,
                full_link=link
        )

    new_link = await creating_link(link)
    await insert_link(link, new_link)
    return models.Link(
                short_link=referer + new_link,
                full_link=link
    )


@router.get('/full/')
async def get_full_link(link: str, request: Request) -> models.Link:
    """
    Response full link from cutting_link</br></br>
    link: link which need to find full version
    """
    referer = config('HTTP_PREFIX') + request.headers.get('host') + '/'
    if not (link_obj := await find_full_link(link.replace(referer, ''))):
        raise HTTPException(
            status_code=404,
            detail='Link not found'
        )

    return models.Link(
                short_link=link,
                full_link=link_obj.full_link
    )


@router.delete('/del/')
async def del_link(link: str, request: Request):
    """
    Delete link</br></br>
    link: link which need to delete
    """
    referer = config('HTTP_PREFIX') + request.headers.get('host') + '/'
    if not (link_obj := await find_full_link(link.replace(referer, ''))):
        raise HTTPException(
            status_code=404,
            detail='Link not found'
        )
    await remove_link(link_obj)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'message': 'Link was deleted successes'}
    )
