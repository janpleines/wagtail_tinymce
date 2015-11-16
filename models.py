class ContentPage(Page):
    """
    The CMS template for content pages will be used for general pages
    like Imprint,  T&C etc.
    """

    main_part = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', TinyMCEBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('main_part'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=_('Content')),
        ObjectList(Page.promote_panels, heading=_('SEO')),
        ObjectList(Page.settings_panels, heading=_('Settings'), classname="settings"),
    ])