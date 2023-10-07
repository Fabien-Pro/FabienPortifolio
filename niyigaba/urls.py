from django.urls import path
from . import views
# from .views import index, skills
urlpatterns = [
    # path('admin', admin.site.urls),
    path('', views.index, name="index"),
    path('skills.html', views.skills, name='skills'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
            # path('skills.html', views.skills, name='skills'),
]
