#! /usr/bin/env python
# -*- coding: utf-8 -*-
class professor:
	usuallysay="�ڤ@�I�����|���NXD"
	def Specialty(self):
		print "�M����C�y���B�q������" 
class student(professor): 
	def interesting(self):
		print "���쬰Python"

p=professor()
s=student()
print "�бª�",
p.Specialty()
print "�ǥͪ�",
s.Specialty()
s.interesting()
print p.usuallysay
print s.usuallysay