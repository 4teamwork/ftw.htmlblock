from ftw.htmlblock.tests import FunctionalTestCase
from Products.CMFCore.utils import getToolByName


class TestDefaultProfile(FunctionalTestCase):

    def test_installed(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        version = portal_setup.getLastVersionForProfile('ftw.htmlblock:default')
        self.assertNotEqual(version, None)
        self.assertNotEqual(version, 'unknown')
