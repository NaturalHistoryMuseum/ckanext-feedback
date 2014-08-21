
import ckan.lib.base as base
import ckan.logic as logic
import ckan.model as model
import ckan.plugins as p
from ckan.common import _, request, c
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
            base.abort(401, _('You must log in to with your NHM account details to be able to send feedback.'))

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
            return p.toolkit.render('feedback/form.html', extra_vars=vars)

    def roadmap(self):

        c.releases = [
            {
                'name': 'Private beta',
                'date': 'August 2014',
                'tasks': [
                    # (Feature name, Feature desc, percentage complete)
                    ('KE EMu specimens', 'KE EMu specimen records, to be made available as Darwin Core.\nCreate automated data pipeline to keep data portal in sync with KE EMu.', 100),
                    ('Custom datasets', ' Museum staff can upload their own datasets.', 100),
                    ('Dataset licencing', 'Allow staff to select a licence for their datasets.', 100),
                    ('Dataset metadata', 'Metadata describing the dataset, including authors, abstract, tagging and geospatial extent.', 100),
                    ('Dataset search', 'Search interface for discovering datasets.', 100),
                    ('Dataset versioning / activity', 'Track dataset changes and activity.', 100),
                    ('Dataset metrics', 'Track dataset views and downloads.', 100),
                    ('Tables', 'Tabular interfaces to explore datasets.', 100),
                    ('Geospatial visualisation', 'Interactive visualisation to explore geospatial datasets.', 100),
                    ('Statistics visualisation', 'Explore dataset growth over time.', 100),
                    ('API', 'Provide API to access and query datasets.', 100),
                    ('Download data', 'Data and datasets downloadable. Must be either authenticated user / supply email address.', 100),
                    ('LDAP Integration', 'Museum staff can login with their Museum credentials.', 100),
                    ('Design', 'Custom design for the data portal.', 100),
                    ('Contact forms', 'Interface to contact dataset owners & curatorial staff (for KE EMu specimens).', 100),
                    ('Data issues', 'Mechanism to flag & resolve data issues (the data corrections should happen at source though - e.g. in KE EMu ).', 100),
                    ('Social share links', 'Users can share datasets over Twitter, Facebook and Google+', 100),
                    ('Site statistics', 'Publish site statistics, including number of datasets, contributors and records..', 100),
                    ('Image catalogue', 'Register image library endpoint.', 100),
                    ('Library catalogue', 'Register library catalogue endpoint.', 100),
                ],
                'issues': [
                    ('KE EMu images', 'KE EMu images are being delivered via the old interfaces, so some images are missing. We will switch to using MAMs when it comes online.'),
                    ('DOIs', 'Dataset DOIs are currently just placeholders. The Museum needs to sign up for the British Library\'s DataCite service so we can start minting permanent DOIs.')
                ]

            },
            {
                'name': 'Public beta',
                'date': 'December 2014',
                'tasks': [
                    # (Feature name, Feature desc, percentage complete)
                    ('Museum consultation', 'Revise portal & features based on staff feedback.', 0),
                    ('Museum datasets', 'Identify other Museum and staff datasets to add to the portal.', 0),
                    ('GBIF', 'Publish KE EMu specimen dataset to the GBIF network.', 20),
                    ('Embargo/private datasets', 'Datasets can be marked as private or embargoed until a set date.', 50),
                    ('DOIs', 'Assign DataCite DOIs to all datasets.', 40),
                    ('API documentation', 'API documentation to be made available online.', 0),
                    ('Citation metrics', 'Add citations to dataset metrics.', 0),
                    ('Social metrics', 'Track dataset sharing metrics on social networks (Twitter, Facebook, Google+).', 0),
                    ('Specimen identifiers', 'Stable identifiers on KE EMu specimen records.', 0),
                    ('Deposition guidelines', 'Guidelines for staff as to what data should be made available.', 0),
                    ('Machine readable', 'Machine readable data & metadata (RDF/JSON-LD).', 0),
                    ('Specimen requests', 'Work with collections & curatorial staff to identify who should receive contact requests for specimens.', 0),
                ],
            },
            {
                'name': 'Full launch',
                'date': '2015',
                'tasks': [
                    ('Data versioning', 'Version data to allow track changes.', 0),
                    ('Subsets', 'Create datasets based on subsets of other datasets (e.g. KE EMu).', 0),
                    ('R Integration', 'Data portal datasets queryable in R.', 0),
                    ('Enhanced visualisations', 'Enhanced data visualisations, including statistical and geochemical (TAS).', 0),
                    ('Geospatial enhancements', 'Alternative map projections; layers, and interactive map timelines.', 0),
                    ('Metagenomics data', 'Make Museum\'s metagenomics data available via the portal.', 0),
                ]

            },
        ]

        return p.toolkit.render('feedback/roadmap.html')

