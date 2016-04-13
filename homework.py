#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
username=raw_input("請輸入會員卡號，卡號格式為１個大寫英文字－6碼數字:")
while re.findall(r"[A-Z]-\d{6}",username)==[]:
	username=raw_input("請重新輸入會員卡號，格式為１個大寫英文字－6碼數字：")

ans="E-056790"
if username==ans:
	print "恭喜您中獎！金額為:10萬"
elif re.findall(r"E-\d56790",username)!=[]:
	print "恭喜您中獎！金額為:2萬"
elif re.findall(r"[A-Z]-\d{3}790",username)!=[]:
	print "恭喜您中獎！獎品為:100元購物禮券"
else:

	print "~銘謝惠顧~"