from rest_framework.permissions import BasePermission


class IsMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        if obj in request.user.member.all():
            print(f'True')
            return True
        else:
            print(f'False')
            return False
