from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig


class FtwHtmlBlockLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)
        z2.installProduct(app, 'ftw.simplelayout')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ftw.htmlblock:default')


FTW_HTMLBLOCK_FIXTURE = FtwHtmlBlockLayer()

FTW_HTMLBLOCK_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FTW_HTMLBLOCK_FIXTURE, ),
    name="ftw.htmlblock:functional")
