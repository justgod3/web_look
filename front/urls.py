from  django.urls import path
from . import views
app_name = 'front'


urlpatterns = [
    path("", views.index, name="index"),
    path("file/",views.file,name="file"),
    path("test/<path:path>/",views.test,name="test"),
    path("go/",views.go,name="go"),
    path("error/",views.error,name="error"),
    path("meiyu/",views.meiyu,name="meiyu"),
    path("go_on/",views.go_on,name="go_on"),
    path("sheetname/",views.sheetname,name="sheetname"),
    path("del_file/",views.del_file,name="del_file"),
    path("text/",views.text,name="text"),
    path("time/",views.tim,name="time"),
]