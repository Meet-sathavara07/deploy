from django.contrib import admin
from .models import newsletter
from .models import Contact
from .models import JobApplication
from .models import SpaceImg
from .models import EmsImg
from .models import AcvImg
# Register your models here.
admin.site.register(newsletter)
admin.site.register(Contact)
admin.site.register(JobApplication)
admin.site.register(SpaceImg)
admin.site.register(EmsImg)
admin.site.register(AcvImg)