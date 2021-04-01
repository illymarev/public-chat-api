from .views import ChatMessageViewSet
from rest_framework.routers import DefaultRouter

app_name = 'chat'
router = DefaultRouter()

router.register('chat', ChatMessageViewSet)

urlpatterns = router.urls
