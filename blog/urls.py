from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path("<slug:category>/<slug:slug>/", views.PostDetailView.as_view(), name="detail_post"),
    path("<slug:category_slug>", views.CherryPickView.as_view(), name="category"),
    path("tag/<slug:slug>", views.CherryPickView.as_view(), name="tag"),
    path("", views.CherryPickView.as_view()),
    path('pages/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)