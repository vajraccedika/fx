from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    #only owners can edit obj

		def has_object_permission(self, request, view, obj):
			# Read permissions allowed to any request
			# so allow GET, HEAD, OPTIONS requests
			if request.method in permissions.SAFE_METHODS:
				return True
			
			# write permissions only allowed to owner of transaction
			return obj.owner == request.user