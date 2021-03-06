from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from .views import product_list_view,product_create_view,product_edit_view,product_view,product_delete_view
from .views import product_list_view,product_create_view,product_edit_view,product_view,product_delete_view,upload_pic

urlpatterns = [
	path('list/', product_list_view, name='product-list'),
	path('create/', product_create_view, name='product-create'),
	path('<int:id>/edit/', product_edit_view, name='product-edit'),
	path('<int:id>/view/', product_view, name='product-view'),
	path('<int:id>/delete/', product_delete_view, name='product-delete'),
	path('upload_pic/', upload_pic, name='upload_pic'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)