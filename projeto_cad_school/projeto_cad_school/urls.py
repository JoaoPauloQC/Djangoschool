

from django.urls import path
from app_cad_school import views


urlpatterns = [
    #rota, view responsavel, nome de referencia
    # exemplo.com
    path('', views.home,name="home"),

    path('informacoes/', views.informacoes , name='informacoes' )
    # exemplo.com/joao
    # path('joao/')
]
