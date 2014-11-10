#!/usr/bin/python2.7
#######################################
#
# This program pulls the current build from Github using Pookie.
# RA Sims II
# 11.08.2014
# @mantisOrange
# orangemantis.net
# license: MIT
#
#######################################

from pookie import Pookie

#Declare repo host
projecthost = 'raw.githubusercontent.com'
#Declare root of project
projectroot = '/orangemantis/deebs/master/'      
# Declare a save path to save file1 to
savepath = '../deebsjs.com/downloads/'


#Instantiate pookie
pk = Pookie(projecthost)


#Request package json
config = pk.fetchconfig(projectroot + 'package.json', 443)
#Use package data to construct a file path
loc1 = projectroot + config['main']


#A name for the file to be saved
savename = config['name'] + '.' + config['version'] + '.js'
#Get the target file
result1 = pk.fetch(loc1, 443, True, savename, savepath)

#Get the minified file
filename2 = config['name'] + '.' + config['version'] + '.min.js'
loc2 = projectroot + config['name'] + '-build/' + filename2
result2 = pk.fetch(loc2, 443, True, filename2, savepath)

if (result1 and result2):
    print 'Pookie ran successfully.'
else:
    print 'Pookie failed!'