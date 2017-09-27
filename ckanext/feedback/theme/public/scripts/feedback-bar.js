/* Table toggle more
 * When a table has more things to it that need to be hidden and then shown more
 */
this.ckan.module('feedback-bar', function ($, _) {
    var self;
    var cookieName = 'feedback-bar-collapsed-dep';
    return {

        /* Initialises the module setting up elements and event listeners.
         *
         * Returns nothing.
         */
        initialize: function () {
            self = this;
            var collapsed = $.cookie(cookieName);

            // Hidden in CSS. SHow if cookie is not set
            if (!collapsed) {
                self.show()
            }

            // Set the cookie after showing once, so we don't irritate people too much
            // self.setCookie();

            $('div#feedback-bar-close', self.el).click(self.close)

        },

        close: function (e) {
            e.preventDefault();
            self.hide();
            $('div#feedback-bar-close', self.el).hide();
            self.setCookie();
        },

        setCookie: function (e) {
            $.cookie(cookieName, true, {path: '/'});
        },

        show: function (e) {
            self.el.animate({
                left: "0"
            }, 600);
            // On show, display the close button
            $('div#feedback-bar-close', self.el).show();
        },

        hide: function (e) {
            self.el.animate({
                left: "-200"
            }, 150);
        }

    }

});