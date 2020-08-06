"""RS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url

from . import view
from . import item
from . import data
from . import username
from . import saveitem
from . import savedata
from . import result

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^item/$', item.get),                      #为保存item提供可查询的数据
    url(r'^item_save/$', saveitem.save),            #保存item数据
    url(r'^data/$', data.get),                      #为保存data提供可查询的数据
    url(r'^data_save/$', savedata.save),            #保存data数据
    url(r'^username/$', username.get),              #为rs推荐提供可查询的数据
    url(r'^result/$', result.get),                  #rs推荐，返回用户id和电影名称和电影id
]