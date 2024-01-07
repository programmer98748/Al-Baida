from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth import views as auth_views
from dashboard.views import ChangePasswordView
from dashboard import views as X
from users import views as V
from django.conf.urls import handler404, handler500



urlpatterns = [
    path('dashboard/', include('dashboard.urls', namespace = 'dashboard')),

    path('', include('website.urls')),

    path('dashboard/login/', V.login_view, name='login'),
    path("logout/", X.auth_logout, name="logout"),
    path('admin/', admin.site.urls),
    path('dashboard/password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

#handler404 = 'website.views.handel404'
#handler500 = 'website.views.handel500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
