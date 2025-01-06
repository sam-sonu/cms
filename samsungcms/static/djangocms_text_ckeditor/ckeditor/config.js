/**
 * @license Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function (config) {
    // Define changes to default configuration here. For example:
    // config.language = 'fr';
    // config.uiColor = '#AADC6E';
    // config.protectedSource.push(/<i class[\s\S]*?\>/g);
    // config.protectedSource.push(/<\/i>/g);
    config.extraPlugins = 'fontawesome';
    config.contentsCss = '/static/all.css';
    config.toolbar = [
        {name: 'insert', items: ['FontAwesome', 'Source']}
    ];
    config.allowedContent = true;
    config.protectedSource.push(/<i class="fa[s|r|l|b] [A-Za-z0-9\-]+"><\/i>/g);
};
CKEDITOR.dtd.$removeEmpty['i'] = false;