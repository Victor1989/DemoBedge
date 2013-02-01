from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class BedgedemositebadgeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import Bedge.demositebadge
        xmlconfig.file(
            'configure.zcml',
            Bedge.demositebadge,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')


BEDGE_DEMOSITEBADGE_FIXTURE = BedgedemositebadgeLayer()
BEDGE_DEMOSITEBADGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BEDGE_DEMOSITEBADGE_FIXTURE,),
    name="BedgedemositebadgeLayer:Integration"
)
