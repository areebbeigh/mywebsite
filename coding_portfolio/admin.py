from django.contrib import admin
from .models import *


################################################################################
#                                                                              #
#    Copyright (C) 2016  Areeb Beigh <areebbeigh@gmail.com>                    #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version.                                       #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
################################################################################


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        # ('Date Information', {'fields': ['publish_date'], 'classes': ['collapse']}), # NOT EDITABLE
        ('Project Information', {'fields': ['name', 'description', 'languages', 'thumbnail']}),
    ]
    list_display = ('name', 'publish_date')
    list_filter = ['publish_date']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(About)
