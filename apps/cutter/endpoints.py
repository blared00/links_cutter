from fastapi import HTTPException, status, APIRouter
from fastapi.responses import JSONResponse

from .utils import check_link, creating_link, insert_link, find_short_link, remove_link, find_full_link

router = APIRouter(
    prefix='/cutter',
    tags=['Cutter'],
)


@router.get('/cut/')
async def create_short_link(link: str):
    """
    Get cutting link</br></br>

    link: link which need to cut
    """
    if not await check_link(link):
        raise HTTPException(
            status_code=400,
            detail='Bad link. Can you double check link and send again?'
        )

    if exist_link := await find_short_link(link):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'new_link': exist_link.short_link}
        )

    new_link = await creating_link(link)
    await insert_link(link, new_link)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={'new_link': new_link}
    )


@router.get('/full/')
async def get_full_link(link: str):
    """
    Response full link from cutting_link</br></br>
    link: link which need to find full version
    """

    if not (link_obj := await find_full_link(link)):
        raise HTTPException(
            status_code=404,
            detail='Link not found'
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'full_link': link_obj.full_link}
    )


@router.delete('/del/')
async def del_link(link: str):
    """
    Delete link</br></br>
    link: link which need to delete
    """
    if not (link_obj := await find_full_link(link)):
        raise HTTPException(
            status_code=404,
            detail='Link not found'
        )
    await remove_link(link_obj)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'message': 'Link was deleted successes'}
    )
