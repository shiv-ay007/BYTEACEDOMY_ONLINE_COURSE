from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('lectures/', views.lectures),
    path('lecturecat/',views.lecturecat),
    path('enotes/', views.enotes),
    path('profile/', views.profile),
    path('category/', views.mycategory),
    path('signout/', views.signout),
    path('softwarekit/', views.software),
    path('task/', views.task),
    path('tsubmitted/',views.tsubmitted),
    path('python/',views.python),
    path('bootstrap/',views.bootstrap),
    path('java/',views.java),
    path('csharp/',views.csharp),
    path('clanguage/',views.clanguage),
    path('php/',views.php),
]
