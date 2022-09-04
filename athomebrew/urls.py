from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"

urlpatterns = [
    path("login_register/", views.login_register, name="login_register"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("home/", views.home, name="home"),
    path("courses/", views.coursePage, name="courses"),
    path("you_courses/", views.you_coursePage, name="you_courses"),
    path("user/", views.userPage, name="user"),
    path("search/", views.searchPage, name="search"),
    path("tt/", views.ttPage, name="tt"),
    path("display/<str:id_course>", views.displayPage),
    path("display/<str:id_course>/quiz", views.quizPage),
    path("results/", views.resultsPage, name="results")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
