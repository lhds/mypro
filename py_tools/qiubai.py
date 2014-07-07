# -*- coding: utf-8 -*-
# 糗百命令行版
#
#

import requests
import re

class qiubai:
	def __init__(self, page=1):
		self.page = page

	def search(self, page):
		url = 'http://www.qiushibaike.com/week/page/%s' % page
		re_qb = re.compile(r'<div class="content" title=".*?">(.*?)</div>', re.DOTALL)
		html = requests.get(url)
		my_qiubai = re_qb.findall(html.text)
		count = 3
		for e in my_qiubai:
			if count == 0:
				o = raw_input()
				if o == 'q':
					exit()
				count = 3
			print e.encode('gb18030')
			count -= 1
		s = raw_input()
		if s == 'q':
			exit()
		else:
			page = int (page) + 1
			print ('-'*18 + '第' + str(page) + '页' + '-'*18).decode('utf-8').encode('gb18030')
			self.search(page)
	
	def query(self):
		global p
		p = raw_input('输入要看的页数:'.decode('utf-8').encode('gb18030'))
		if p == 'q':
			exit()
		elif not p.isdigit() or p == '0':
			self.query()
		else:
			print ('-'*18 + '第' + p + '页' + '-'*18).decode('utf-8').encode('gb18030')
			self.search(p)

if __name__ == '__main__':
	print '-'.decode('utf-8').encode('gb18030')*41
	print '糗百命令行版'.decode('utf-8').encode('gb18030')
	print '输入q退出程序，回车继续'.decode('utf-8').encode('gb18030')
	print '-'.decode('utf-8').encode('gb18030')*41
	qb = qiubai()
	qb.query()

