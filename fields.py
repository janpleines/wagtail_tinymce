# coding=utf-8
from django import forms
from wagtail.utils.widgets import WidgetWithScript
from wagtail.wagtailcore.rich_text import expand_db_html, DbWhitelister


class TinyMCEArea(WidgetWithScript, forms.Textarea):
    def get_panel(self):
        from wagtail.wagtailadmin.edit_handlers import RichTextFieldPanel
        return RichTextFieldPanel

    def render(self, name, value, attrs=None):
        if value is None:
            translated_value = None
        else:
            translated_value = expand_db_html(value, for_editor=True)
        return super(TinyMCEArea, self).render(name, translated_value, attrs)

    def render_js_init(self, id_, name, value):
        return 'registerField("'+name+'");'

    def value_from_datadict(self, data, files, name):
        original_value = super(TinyMCEArea, self).value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return DbWhitelister.clean(original_value)
