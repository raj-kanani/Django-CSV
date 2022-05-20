from django.conf import settings
from django.urls import path
from .import views
from django.conf.urls.static import static


urlpatterns = [
    path('csv/', views.export_to_csv, name='csv'),
    path('csv1/', views.generate_csv, name='csv1'),

    path('m1/', views.csv_simple_write, name='m1'),
    path('m2/', views.csv_dictionary_write, name='m2'),
    path('m3/', views.csv_database_write, name='m3'),
    path('m4/', views.csv_simple_read, name='m4'),
    path('m5/', views.CSVPageView.as_view(), name='m5'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


