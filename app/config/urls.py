
#from django.contrib import admin
#from django.urls import include, path

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url

import ppd.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('theses/', include('thesius.urls'), name='theses'),
    path('', ppd.views.main_view),
    path('profile/u<slug:pk>', ppd.views.profile, name='url_profile'),
    path('profile/u<slug:pk>/edit', ppd.views.profile_edit, name='url_profile_edit'),
    path('unitys/', ppd.views.unitys, name='url_unitys'),
    path('test/', ppd.views.test),
    path('ind_thesis_norm/', ppd.views.ind_thesis_norm),
    path('unitys/un<slug:pk>/', ppd.views.unity, name='url_unity'),
    path('unitys/un<slug:pk>/edit/', ppd.views.unity_edit, name='url_unity_edit'),
    path('unitys/un<slug:uni>/m<slug:pk>/', ppd.views.message, name='url_msg'),#th<slug:pk>/
    path('unitys/un<slug:uni>/th<slug:pk>/', ppd.views.thesisreply, name='url_thes'),#th<slug:pk>/
    #path('accounts/register/', ppd.MyRegisterFormView.as_view(), name="register"),

    url(r'^accounts/register/$', ppd.views.MyRegisterFormView.as_view(), name='register'),
    path('accounts/login/', ppd.views.login2),
    
    path('ajax/send_post/', ppd.views.ajax_sendpost),
    path('ajax/editpost/', ppd.views.ajax_editpost),
    path('ajax/savepost/', ppd.views.ajax_savepost),
    path('ajax/unitys_list/', ppd.views.ajax_unitys_list),
    path('ajax/reply_list/', ppd.views.ajax_replys_list),
    path('ajax/unitys_create/', ppd.views.ajax_unitys_create),
    path('ajax/msg_send/', ppd.views.ajax_msg_send),
    path('ajax/like_send/', ppd.views.ajax_like_send),
    path('ajax/thesislike_send/', ppd.views.ajax_thesislike_send),
    path('ajax/inicho_send/', ppd.views.ajax_inicho_send),
    path('ajax/thesis_send/', ppd.views.ajax_thesis_send),
    path('ajax/userreply_send/', ppd.views.ajax_userreply_send),
    path('ajax/unity_picture/', ppd.views.ajax_unity_picture),
    path('ajax/registration/', ppd.views.ajax_registration),
    path('ajax/authorization/', ppd.views.ajax_authorization),
    path('ajax/ini_create/', ppd.views.ajax_ini_create),
    path('ajax/ini_getform/', ppd.views.ajax_ini_getform),
    path('ajax/msg_viewed/', ppd.views.ajax_msg_viewed),
    path('ajax/thes_viewed/', ppd.views.ajax_thes_viewed),
    path('ajax/taglist/', ppd.views.ajax_taglist),
    path('ajax/thesiscateglist/', ppd.views.ajax_thesiscateglist),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

