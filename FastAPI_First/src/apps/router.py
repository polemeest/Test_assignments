
from fastapi import APIRouter

from apps.lovers.views import router as l_router
from apps.complex.views import router as c_router
from apps.singletons.views import router as s_router

router = APIRouter()

router.include_router(l_router)
router.include_router(c_router)
router.include_router(s_router)
