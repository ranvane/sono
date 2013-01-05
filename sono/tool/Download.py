# -*- encoding:utf-8 -*-
'''
Created on 2012-12-20

@author: ranvane

www.ranblog.info
'''
import urllib, urllib2
import gzip, StringIO
class Download(object):
    '''
    classdocs
    '''
     
    def download_Page_By_Url(self, url,code):
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0') 
        request.add_header('Referrer', url)
        retval = urllib2.urlopen(request)
         
        #print retval.headers
         
        context = ''
        if retval.headers.has_key('content-encoding'):
            fileobj = StringIO.StringIO()
            fileobj.write(retval.read())
            fileobj.seek( 0)
            gzip_file = gzip.GzipFile(fileobj=fileobj)
            context = gzip_file.read()
        else:
            context = retval.read()
        if code:
            context = unicode(context,code)
        else:
            context = unicode(context,'utf8')
        return context
         