from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Services)
admin.site.register(SubServices)
admin.site.register(Portfolio)
admin.site.register(Pricing)
admin.site.register(Queries)
admin.site.register(Contact)
admin.site.register(Logo)
admin.site.register(Navigation)
admin.site.register(Slide)
admin.site.register(SlideInfo)
admin.site.register(TermsAndConditions)


admin.site.site_header = "Photo Resolve Admin Panel"
admin.site.site_title = "Photo Resolve  Admin Portal"
admin.site.index_title = "Welcome to Photo Resolve  Portal"