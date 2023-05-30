from django.contrib.auth.models import User
from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class UserEditWindow(BaseEditWindow):
    """Окно для создания/редактирования пользователя."""

    def _init_components(self):
        """Создание компонентов."""

        super()._init_components()

        self.field__username = ext.ExtStringField(
            label='Username', name='username',
            allow_blank=False, anchor='100%'
        )

        self.field__email = ext.ExtStringField(
            label='Email', name='email',
            allow_blank=False, anchor='100%'
        )

        self.field__first_name = ext.ExtStringField(
            label='First name', name='first_name', anchor='100%'
        )

        self.field__last_name = ext.ExtStringField(
            label='Last name', name='last_name', anchor='100%'
        )

        self.field__active = ext.ExtCheckBox(
            label='Active', name='is_active',
        )

        self.field__staff = ext.ExtCheckBox(
            label='Staff', name='is_staff',
        )

        self.field__superuser = ext.ExtCheckBox(
            label='Superuser', name='is_superuser',
        )

        self.field__date_joined = ext.ExtDateField(
            label='Date joined', name='date_joined',
            anchor='100%', format='d.m.Y'
        )

        self.field__last_login = ext.ExtDateField(
            label='Last login', name='last_login',
            anchor='100%', format='d.m.Y'
        )

        self.field__password = ext.ExtStringField(
            label='Password', name='password',
            anchor='100%', allow_blank=False,
        )

    def _do_layout(self):
        """Настройка расположения компонентов."""

        super()._do_layout()
        self.form.items.extend([
            self.field__username,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__active,
            self.field__staff,
            self.field__superuser,
            self.field__date_joined,
            self.field__last_login,
            self.field__password,
        ])

    def set_params(self, params):
        """Задание параметров окна."""

        super().set_params(params)
        self.height = 'auto'
