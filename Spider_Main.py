# -*- encoding:UTF-8 -*-

from wiki_spider import Url_Manager
from wiki_spider import Html_Downloader
from wiki_spider import Html_Parser
from wiki_spider import Html_Outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = Url_Manager.Url_Manager()
        self.downloader = Html_Downloader.Html_Downloader()
        self.parser = Html_Parser.Html_Parser()
        self.outputer = Html_Outputer.Html_Outputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print '第%d条URL是:%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(html_cont)
                self.urls.add_new_url(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print 'craw failed'
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://zh.wikipedia.org/wiki/Python'
    obj_Spider = SpiderMain()
    obj_Spider.craw(root_url)
