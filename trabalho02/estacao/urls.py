from django.urls import path
from estacao.views import (
    DataListView
)

urlpatterns = [
    path("", DataListView.as_view(), name="data_list")
]
