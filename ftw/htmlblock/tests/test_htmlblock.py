from ftw.builder import Builder
from ftw.builder import create
from ftw.testbrowser import browsing
from ftw.htmlblock.tests import FunctionalTestCase


class TestHtmlBlock(FunctionalTestCase):

    def setUp(self):
        super(TestHtmlBlock, self).setUp()
        self.grant('Manager')

    @browsing
    def test_block_does_not_render_title_by_default(self, browser):
        """
        This test makes sure that the block does not render its title by
        default.
        """
        content_page = create(Builder('sl content page'))

        create(Builder('html block')
               .titled(u'Title of the HTML block')
               .within(content_page))

        browser.login().visit(content_page)

        self.assertEqual(
            [],
            browser.css('div.ftw-htmlblock-htmlblock .sl-block-content h2')
        )
        self.assertEqual(
            ['TODO: Replace this static placeholder.'],
            browser.css('div.ftw-htmlblock-htmlblock .sl-block-content').text
        )

    @browsing
    def test_block_title_is_rendered(self, browser):
        """
        This test makes sure that the title of the block is rendered when
        told to do so.
        """
        content_page = create(Builder('sl content page'))

        create(Builder('html block')
               .titled(u'Title of the HTML block')
               .having(show_title=True)
               .within(content_page))

        browser.login().visit(content_page)

        self.assertEqual(
            ['Title of the HTML block'],
            browser.css('div.ftw-htmlblock-htmlblock .sl-block-content h2').text
        )
