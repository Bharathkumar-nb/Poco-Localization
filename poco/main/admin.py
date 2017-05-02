from django.contrib import admin
from .models import Course, Module, Assessment, Content, Related, Video, AssessmentSubmission
from .models import Student, CourseProgress, ModuleProgress, AssessmentProgress, VideoProgress, ContentProgress

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
class AssessmentFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ('module name')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'name'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('zero', ('in Module 0')),
            ('one', ('in Module 1')),
            ('two', ('in Module 2')),
            ('three', ('in Module 3')),
            ('four', ('in Module 4')),
            ('five', ('in Module 5')),
            ('six', ('in Module 6')),
            ('seven', ('in Module 7')),
            ('eight', ('in Module 8')),
            ('nine', ('in Module 9')),
            ('ten', ('in Module 10')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'zero':
            return queryset.filter(assessment__module__title__contains = "0. ")
        if self.value() == 'one':
            return queryset.filter(assessment__module__title__contains = "1. ")
        if self.value() == 'two':
            return queryset.filter(assessment__module__title__contains = "2. ")
        if self.value() == 'three':
            return queryset.filter(assessment__module__title__contains = "3. ")
        if self.value() == 'four':
            return queryset.filter(assessment__module__title__contains = "4. ")
        if self.value() == 'five':
            return queryset.filter(assessment__module__title__contains = "5. ")
        if self.value() == 'six':
            return queryset.filter(assessment__module__title__contains = "6. ")
        if self.value() == 'seven':
            return queryset.filter(assessment__module__title__contains = "7. ")
        if self.value() == 'eight':
            return queryset.filter(assessment__module__title__contains = "8. ")
        if self.value() == 'nine':
            return queryset.filter(assessment__module__title__contains = "9. ")
        if self.value() == 'ten':
            return queryset.filter(assessment__module__title__contains = "10. ")


class AssessmentProgressAdmin(admin.ModelAdmin):
    list_display = ('assessment', 'get_name', 'solved')
    search_fields = ['student__user__last_name', 'student__user__first_name']
    list_filter = (AssessmentFilter,)
    model = AssessmentProgress
    ordering = ['assessment']
    def get_name(self, obj):
        return obj.student.user.first_name + ' ' + obj.student.user.last_name
    get_name.short_description = 'Full name'

class UserAdmin(admin.ModelAdmin):
    actions = ['make_inactive','make_active']
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')
    list_filter = ('is_active', )

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected users as inactive"

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected users as active"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Assessment)
admin.site.register(Content)
admin.site.register(Video)
admin.site.register(Related)
admin.site.register(Student)
admin.site.register(CourseProgress)
admin.site.register(ModuleProgress)
admin.site.register(ContentProgress)
admin.site.register(AssessmentProgress,AssessmentProgressAdmin)
admin.site.register(VideoProgress)
admin.site.register(AssessmentSubmission)

