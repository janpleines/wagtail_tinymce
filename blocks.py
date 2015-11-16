# coding=utf-8
from django import forms
from django.utils.encoding import force_text
from django.utils.functional import cached_property
from wagtail.wagtailcore.blocks import FieldBlock
from wagtail.wagtailcore.rich_text import RichText


class TinyMCEBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field_options = {'required': required, 'help_text': help_text}
        super(TinyMCEBlock, self).__init__(**kwargs)

    def get_default(self):
        if isinstance(self.meta.default, RichText):
            return self.meta.default
        else:
            return RichText(self.meta.default)

    def to_python(self, value):
        # convert a source-HTML string from the JSONish representation
        # to a RichText object
        return RichText(value)

    def get_prep_value(self, value):
        # convert a RichText object back to a source-HTML string to go into
        # the JSONish representation
        return value.source

    @cached_property
    def field(self):
        from core.fields import TinyMCEArea
        return forms.CharField(widget=TinyMCEArea, **self.field_options)

    def value_for_form(self, value):
        # TinyMCEBlock takes the source-HTML string as input (and takes care
        # of expanding it for the purposes of the editor)
        return value.source

    def value_from_form(self, value):
        # TinyMCEBlock returns a source-HTML string; convert to a RichText object
        return RichText(value)

    def get_searchable_content(self, value):
        return [force_text(value.source)]

    class Meta:
        classname='tinymce'
        icon = 'placeholder'