from django.conf.urls import url
from AppTwo import views

app_name='AppTwo'

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^form/',views.form_view,name="form"),
    url(r'^help/',views.help,name="help"),
    url(r'^TopicList/',views.Topic_list,name="topics"),
    url(r'^WebpageList/',views.Webpage_list,name="web"),
    url(r'^AccessList/',views.AccessRecord_list,name="access"),
    url(r'^webform/',views.webForm,name="web_form"),
]