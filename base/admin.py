from django.contrib.gis import admin
from base.models import UserProfile
from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite
from django.contrib.admin.forms import AuthenticationForm

class StaffAdmin(admin.GISModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def has_view_permission(self, request, object=None) -> bool:
        return True

    def has_change_permission(self, request, object=None) -> bool:
        return True
    
    def has_module_permission(self, request, object=None) -> bool:
        return True

class UserAdmin(AdminSite):
    """
    App-specific admin site implementation
    """

    login_form = AuthenticationForm


    def has_permission(self, request):
        """
        Checks if the current user has access.
        """
        return request.user.is_active


user_admin_site = UserAdmin(name='usersadmin')

# Register your models here.
admin.site.register(UserProfile, StaffAdmin)
user_admin_site.register(UserProfile, StaffAdmin)
user_admin_site.register(User)
user_admin_site.register(Group)