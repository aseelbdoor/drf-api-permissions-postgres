from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    message = "you can tedit this Thing object , you are not the owner !!"
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        
        if request.user == obj.purchaser :
            return True 
        else : 
            return False 