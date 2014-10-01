__author__ = 'cifer'
from django.db import connection


class DBMiddlware(object):
    def process_response(self, request, response):
        query_time = 0.0
        for query in connection.queries:
            query_time += float(query[u'time'])
        query_num_time = u'Made %s queries in %s sec' % (len(connection.queries), query_time)
        # query_num_time = connection.queries[0][u'time']
        response.content = response.content.replace(u'</body>', u'%s </body>' % query_num_time)
        return response
