from django.urls import path

from . import views

app_name = "polls"
# URLs que van despues del urls patterns del sitio/proyecto
# example.com/<urlspatterns del proyecto>/<urls de la app>
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
"""
    Forma manual de hacerlo
    path("", views.index, name="index"),
    path("tabla/", views.tabla, name="tabla"),
    # este path es el que llama el 'url' del archivo detail.html
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
"""