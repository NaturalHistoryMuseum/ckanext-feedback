/* Table toggle more
 * When a table has more things to it that need to be hidden and then shown more
 */
this.ckan.module('feedback-bar', function ($, _) {
    var self;
    return {

        /* Initialises the module setting up elements and event listeners.
         *
         * Returns nothing.
         */
        initialize: function () {

            self = this;

            var hidden = $.cookie('feedback-bar-hidden');

            // Hidden in CSS. SHow if cookie is not set
            if (!hidden){
                self.el.show();
            }

            $('a.feedback-close', self.el).click(self._close)

        },

        _close: function(e) {
            e.preventDefault();
            self.el.hide();
            $.cookie('feedback-bar-hidden', true);
        }

    }

});