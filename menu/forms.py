from django import forms
from .models import menu_item
from .widgets import GfkLookupWidget


class MenuItemAdminForm(forms.ModelForm):
    """Форма пунктов меню админ панели"""
    class Meta(object):
        model = menu_item
        fields = ('__all__')
        exclude = ("slug",)
        widgets = {
            'object_id': GfkLookupWidget(
                content_type_field_name='content_type',
                parent_field=menu_item._meta.get_field('content_type'),
            )
        }