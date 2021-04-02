from .views import MessageListViewSet, SingleMessageViewSet
from rest_framework.routers import DefaultRouter

app_name = 'chat'
router = DefaultRouter()

router.register('list', MessageListViewSet) # use list/?page=id
router.register('single', SingleMessageViewSet)

urlpatterns = router.urls
