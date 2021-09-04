from django.contrib import admin
from django.utils.translation import ugettext as _

from app.models import Continent, Country, City

admin.site.site_header = _('Geopedia')
admin.site.index_title = _('Administration')
admin.site.site_title = _('Geopedia')

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
