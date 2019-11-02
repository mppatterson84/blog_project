// CKEDITOR.replace('body')
// https://ckeditor.com/docs/ckeditor4/latest/guide/dev_configuration.html
CKEDITOR.replace('body', {
    'extraPlugins': ['codesnippet', 'autogrow',],
    'codeSnippet_theme': 'dark',
    'autoGrow_onStartup': true,
    'autoGrow_minHeight': '300',
    'toolbar': 'Custom',
    'toolbar_Custom': [
        ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
        ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
        ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
        ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
        ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'],
        ['Link', 'Unlink', 'Anchor'],
        ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
        ['Styles', 'Format', 'Font', 'FontSize'],
        ['TextColor', 'BGColor'],
        ['Maximize', 'ShowBlocks'],
        // ['About'],
        ['CodeSnippet'],
    ],
});
