__author__ = 'batulu'
from scrapy import log
class RetryMiddleware(object):
    def process_request(self, request, spider):
        log('Requesting url %s with ' % (request.url))

    def process_response(self, request, response, spider):
        log('Response received from request url %s ' % (request.url))

    def process_exception(self, request, exception, spider):
        #log_msg('Failed to request url %s  with exception %s' % (request.url,str(exception)))
        print '********************************'
        return request