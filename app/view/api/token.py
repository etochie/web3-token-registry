from os.path import exists

from fastapi import APIRouter
from fastapi import HTTPException
from starlette.responses import FileResponse

router = APIRouter()

base_assets_data_folder = '/var/web3-token-registry/cryptocurrency-icons'


@router.get('/assets/detail/{chain_id}/{asset_name}')
async def get_asset_image(chain_id: int, asset_name: str):
    filename = f'{chain_id}-{asset_name}.svg'
    path = f'{base_assets_data_folder}/{filename}'

    if not exists(path):
        raise HTTPException(status_code=404, detail=f'File {filename} not found')
    else:
        return FileResponse(path)

