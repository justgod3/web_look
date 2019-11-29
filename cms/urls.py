from  django.urls import path
from . import views
app_name = 'cms'


urlpatterns = [
    path("angul/",views.angul,name="angul"),
    path("an_test/",views.an_test,name="an_test"),
]