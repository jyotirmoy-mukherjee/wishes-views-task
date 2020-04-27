from django.conf.urls import url
from wishes import views
from rest_framework.urlpatterns import format_suffix_patterns

#update urlpatterns to use both the view implementations for WishList and WishDetail
urlpatterns = [
    url(r'^wishes/$',views.WishList),
    url(r'^wishes/(?P<pk>[0-9]+)/$',views.WishDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)