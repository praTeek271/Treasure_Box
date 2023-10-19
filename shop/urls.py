from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'shop'

urlpatterns = [
    path("", views.index, name="ShopHomePage"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

]+static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += 