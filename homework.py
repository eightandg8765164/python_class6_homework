#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
username=raw_input("�п�J�|���d���A�d���榡�����Ӥj�g�^��r��6�X�Ʀr:")
while re.findall(r"[A-Z]-\d{6}",username)==[]:
	username=raw_input("�Э��s��J�|���d���A�榡�����Ӥj�g�^��r��6�X�Ʀr�G")

ans="E-056790"
if username==ans:
	print "���߱z�����I���B��:10�U"
elif re.findall(r"E-\d56790",username)!=[]:
	print "���߱z�����I���B��:2�U"
elif re.findall(r"[A-Z]-\d{3}790",username)!=[]:
	print "���߱z�����I���~��:100���ʪ�§��"
else:

	print "~���´f�U~"