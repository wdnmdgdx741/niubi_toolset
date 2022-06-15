#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree

xml ='''
<book>
    <id>1</id>
    <name>野花遍地</name>
    <price>1.1</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">张三</nick>
        <nick id="10010">李四</nick>
        <nick id="jack">王五</nick>
        <div>
            <nick>开心</nick>
        </div>
    </author>
</book>
'''

tree = etree.XML(xml)
result = tree.xpath("/book/name/text()")
#result = tree.xpath("/book/author/*/nick/text()")     *通配符表示任意但不是空，所以匹配不到张三……
#result = tree.xpath("/book/author//nick/text()")      //表示author下所有子类为nick的内容
print(result)




