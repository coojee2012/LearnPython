# _*_ coding: utf-8 _*_

import re

from lxml import etree
from lxml.html import fromstring, tostring
from pyquery import PyQuery as pq

class Selector:
    def __init__(self, rule, attr=None,r_type=None):
        self.rule = rule
        self.attr = attr
        self.r_type = r_type

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.rule)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.rule)

    def parse_detail(self, html):
        raise NotImplementedError


class Css(Selector):
    def parse_detail(self, html):
        d = pq(html)
        if self.attr is None:
            try:
                return d(self.rule)[0].text
            except IndexError:
                return None
        return d(self.rule)[0].attr(self.attr, None)


class Xpath(Selector):
    def parse_detail(self, html):
        d = etree.HTML(html)
        try:
            if self.attr is None:
                result = None
                if len(d.xpath(self.rule)) > 1:
                    result =  [entry for entry in d.xpath(self.rule)]
                else:
                    result = d.xpath(self.rule)

                if self.r_type == 'elstr' and len(result) > 0:
                    return [tostring(el,'utf-8').decode('utf-8') for el in result]
                elif self.r_type == 'text' and len(result) >0:
                    return [el.text for el in result]
                else:
                    return result

            return [entry.get(self.attr, None) for entry in d.xpath(self.rule)] if len(d.xpath(self.rule)) > 1 else \
                d.xpath(self.rule)[0]
        except IndexError:
            return None


class Regex(Selector):
    def parse_detail(self, html):
        try:
            return re.findall(self.rule, html)[0]
        except IndexError:
            return None



