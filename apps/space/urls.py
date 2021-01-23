from rest_framework import routers

from .views import FolderViewSet, ListViewSet, SpacesViewSet

router = routers.SimpleRouter()
router.register(r'space', SpacesViewSet)
router.register(r'folder', FolderViewSet)
router.register(r'list', ListViewSet)

urlpatterns = router.urls