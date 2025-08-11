class RoleBasedAdminMixin:
    allowed_roles_view = []
    allowed_roles_add = []
    allowed_roles_change = []
    allowed_roles_delete = []

    def has_module_permission(self, request):
        return request.user.role in self.allowed_roles_view

    def has_view_permission(self, request, obj=None):
        return request.user.role in self.allowed_roles_view

    def has_add_permission(self, request):
        return request.user.role in self.allowed_roles_add

    def has_change_permission(self, request, obj=None):
        return request.user.role in self.allowed_roles_change

    def has_delete_permission(self, request, obj=None):
        return request.user.role in self.allowed_roles_delete