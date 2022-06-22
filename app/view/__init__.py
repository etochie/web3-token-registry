from fastapi import APIRouter

from view.api import check
from view.api import token

router = APIRouter()

router.include_router(check.router, tags=['check'])
router.include_router(token.router, tags=['token'])
