from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()

base_assets_data_folder = '/var/assets-collector/cryptocurrency-icons'


@router.get('/assets/detail/{chain_id}/{asset_name}', response_class=FileResponse)
async def get_asset_image(chain_id: int, asset_name: str):
    path = f'{base_assets_data_folder}/svg/icon/{chain_id}-{asset_name}.svg'
    return path
