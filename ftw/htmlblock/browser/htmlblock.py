from ftw.simplelayout.browser.blocks.base import BaseBlock


class HtmlBlockView(BaseBlock):
    def __call__(self):
        return self.index()
