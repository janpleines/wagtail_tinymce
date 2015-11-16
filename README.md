# wagtail_tinymce

1. create new field block TinyMCEBlock (blocks.py)

2. create a new field TinyMCEArea (fields.py)

3. overwrite wagtails admin editor javascript (_editor_js.html)

    add tinymce js

    add wagtail internal link support to tinymce

    render editor only on user click

    some random customization for our needs
 
4. add new field block to page model (models.py)
