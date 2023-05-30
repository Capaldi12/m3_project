from django.contrib.auth.models import User, Group, Permission, ContentType
from django.contrib.auth.hashers import make_password, identify_hasher
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .controller import observer
from .ui import UserEditWindow


class UserActionPack(ObjectPack):
    """Управление пользователями."""

    url = '/user'

    model = User
    add_to_menu = True

    # Отображаемые в табличке колонки
    columns = [
        {'header': 'Username', 'data_index': 'username'},
        {'header': 'Email', 'data_index': 'email'},
        {'header': 'First name', 'data_index': 'first_name'},
        {'header': 'Last name', 'data_index': 'last_name'},
        {'header': 'Active', 'data_index': 'is_active'},
        {'header': 'Staff', 'data_index': 'is_staff'},
        {'header': 'Superuser', 'data_index': 'is_superuser'},
        {'header': 'Date joined', 'data_index': 'date_joined'},
        {'header': 'Last login', 'data_index': 'last_login'},
        {'header': 'Password', 'data_index': 'password'},
    ]

    # Окно для добавления и редактирования
    add_window = edit_window = UserEditWindow

    def save_row(self, obj, create_new, request, context, *args, **kwargs):
        """
        Действия при сохранении. Используется чтобы захешировать
        новый пароль при необходимости.
        """

        try:
            # Так проверяется в самом Django
            identify_hasher(obj.password)
        except ValueError:
            # Если хешер найти не удалось, то в поле был введён новый пароль
            # и его надо захешировать
            obj.password = make_password(obj.password)

        super().save_row(obj, create_new, request, context, *args, **kwargs)


class GroupActionPack(ObjectPack):
    """Управление группами пользователей."""

    url = '/group'

    model = Group
    add_to_menu = True

    add_window = edit_window = \
        ModelEditWindow.fabricate(model, model_register=observer)


class PermissionActionPack(ObjectPack):
    """Управление разрешениями пользователей."""

    url = '/permission'

    model = Permission
    add_to_menu = True

    add_window = edit_window = \
        ModelEditWindow.fabricate(model, model_register=observer)


class ContentTypeActionPack(ObjectPack):
    """Управление типами контента."""

    url = '/content_type'

    model = ContentType
    add_to_menu = True

    add_window = edit_window = \
        ModelEditWindow.fabricate(model, model_register=observer)
