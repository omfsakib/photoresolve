
from django.urls import path,include
from .views import *

urlpatterns = [
    path('getServices/',getServices,name="get-services"),
    path('getService/<str:name>',getService,name="get-service"),
    path('getPortfolio/',getPortfolio,name="get-portfolio"),
    path('getPricing/',getPricing,name="get-pricing"),
    path('getContact/',getContact,name="get-contact"),
    path('getLogo/',get_logo,name="get-logo"),
    path('getNavigation/', get_navigation, name='get_navigation'),
    path('getSlideText/', get_slide_text, name='get_slide_text'),
    path('getSlideInfo/', get_slide_info, name='get_slide_info'),
    path('getFooterInfo/', get_footer_info, name='get_footer_info'),
    path('getTermsAndConditions/', get_terms, name='get_terms'),
    path('postQuery/',post_query,name="post-query"),
    path('upload/',upload_file,name="post-image"),
    path('',home,name='home'),
    path('edit/service/<str:pk>',editService,name='edit-service'),
    path('edit/sub-service/<str:pk>',editSubService,name='edit-sub-service'),
    path('edit/pricing/<str:pk>',editPricing,name='edit-pricing'),
    path('edit/portfolio/<str:pk>', editPortfolio,name='edit-portfolio'),
]