#url - view - template


from django.urls import path, include
from .views import Homepage, Projects, Detailprojects

app_name = 'projects'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('projetos/', Projects.as_view(), name='projects'),
    path('projetos/<int:pk>', Detailprojects.as_view(), name='detailprojects'),
]