
import ckan.lib.base as base
import ckan.logic as logic
import ckan.model as model
import ckan.plugins as p
from ckan.common import _, request
from ckanext.contact.controllers.contact import ContactController

check_access = logic.check_access

class FeedbackController(ContactController):
    """
    Controller for displaying a feedback form
    """
    def __before__(self, action, **env):

        super(ContactController, self).__before__(action, **env)

        try:
            self.context = {'model': model, 'session': model.Session, 'user': base.c.user or base.c.author, 'auth_user_obj': base.c.userobj}
            check_access('send_feedback', self.context)
        except logic.NotAuthorized:
            base.abort(401, _('You must log into send feedback.'))


    def form(self):

        """
        Return a contact form
        :return: html
        """

        data = {}
        errors = {}
        error_summary = {}

        # Submit the data
        if 'save' in request.params:
            data, errors, error_summary = self._submit(self.context)
        else:
            # Try and use logged in user values for default values
            try:
                data['name'] = base.c.userobj.fullname or base.c.userobj.name
                data['email'] = base.c.userobj.email
            except AttributeError:
                data['name'] = data['email'] = None

        if data.get('success', False):
            return p.toolkit.render('contact/success.html')
        else:
            vars = {'data': data, 'errors': errors, 'error_summary': error_summary}
            return p.toolkit.render('feedback/page.html', extra_vars=vars)