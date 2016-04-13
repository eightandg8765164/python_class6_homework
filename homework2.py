#! /usr/bin/env python
# -*- coding: utf-8 -*-
class professor:
	usuallysay="我一點都不會介意XD"
	def Specialty(self):
		print "專長為C語言、電腦網路" 
class student(professor): 
	def interesting(self):
		print "興趣為Python"

p=professor()
s=student()
print "教授的",
p.Specialty()
print "學生的",
s.Specialty()
s.interesting()
print p.usuallysay
print s.usuallysay