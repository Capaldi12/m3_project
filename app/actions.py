from django.contrib.auth.models import User, Group, Permission, ContentType
from m3.actions import ActionPack
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow


class UserActionPack(ObjectPack):
    url = '/user'

    model = User
    add_to_menu = True

    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = add_window


class GroupActionPack(ObjectPack):
    url = '/group'

    model = Group
    add_to_menu = True

    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = add_window


class PermissionActionPack(ObjectPack):
    url = '/permission'

    model = Permission
    add_to_menu = True

    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = add_window


class ContentTypeActionPack(ObjectPack):
    url = '/content_type'

    model = ContentType
    add_to_menu = True

    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = add_window
