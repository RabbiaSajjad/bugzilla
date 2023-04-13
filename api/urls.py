from django.urls import path, include

from api.views.base_view import BaseView
from api.views.project_view import ProjectView
from api.views.user_view import UserView
from api.views.bug_view import BugView

urlpatterns = [
    path('projects', ProjectView.as_view(http_method_names=['post', 'get'])),
    path('projects/<int:id>', ProjectView.as_view(http_method_names=['put', 'get', 'delete'])),
    path('users', UserView.as_view(http_method_names=['post', 'get'])),
    path('users/<int:id>', UserView.as_view(http_method_names=['put', 'get', 'delete'])),
    path('bugs', BugView.as_view(http_method_names=['post', 'get'])),
    path('bugs/<int:id>', BugView.as_view(http_method_names=['put', 'get', 'delete'])),
]
