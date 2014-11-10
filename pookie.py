
#######################################
#
# This Class is a utility to pull files from the web, especially Github
# Pookie is named after Chris Rock's errand boy Character in the film New Jack City.
# RA Sims II
# 11.08.2014
# @mantisOrange
# orangemantis.net
# license: MIT
#
#######################################

import httplib
import json

class Pookie:
    def __init__(self, host =''):
        self.config = None
        if(host != '' and isinstance(host, basestring)):
            self.host = host
        else:
            self.host = ''
    
    def fetch(self, loc = '', port = 80, saveflag = False, filename = '', savepath = ''):
        if(loc != '' and isinstance(loc, basestring) and self.host != ''):
            try:
                if (port == 443):
                    conn = httplib.HTTPSConnection(self.host, port)
                else: 
                    conn = httplib.HTTPConnection(self.host, port)
                    
                conn.request('GET', loc)
                resp = conn.getresponse()
                resp = resp.read()
                conn.close()
                if (saveflag == True):
                    self.save(filename, resp, savepath)
                return resp
                
            except httplib.HTTPException as err:
                print 'Could not connect error: ' + err
                return False
        return False

    def fetchconfig(self, loc = '', port = 80):
        config = self.fetch(loc, port)
        if (config != False):
            config = json.loads(config)
            self.config = config
            return config
        return False
    
    def save(self, filename = '', content = '', savepath = ''):
        if ((filename != '' and isinstance(filename, basestring)) 
            and (content != '' and isinstance(content, basestring)) 
            and isinstance(savepath, basestring)):
            filepath = savepath + filename
            with open(filepath, 'w') as savefile:
                savefile.write(content)
                savefile.close()