# logstash-2016.05.01
from datetime import datetime
from elasticsearch import Elasticsearch
import datetime
import logging
# import requests

# curl -XDELETE '10.24.154.234:9200/logstash-2016.04.10?pretty'
# 05.04
# 04.12
# print('http://10.24.xx.xx:9200/logstash-%s?pretty' % str_d )
# r = requests.delete('http://10.24.154.234:9200/logstash-%s?pretty' % str_d )
# print r.text
# f = urllib2.urlopen('http://10.24.154.234:9200/logstash-%s?pretty' % str_d )
def log_str():
	n = datetime.datetime.now()
	# print n.strftime('%Y.%m.%d')
	delta = datetime.timedelta(days=-20)
	str_d = (n+delta).strftime('%Y.%m.%d')
	return 'logstash-' + str_d	

def main():
	# logging.basicConfig(format='%(asctime)s %(message)s')
	tracer = logging.getLogger('elasticsearch.trace')
	# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	# tracer.setFormatter(formatter)
	tracer.setLevel(logging.INFO)
	tracer.addHandler(logging.FileHandler('/tmp/es_trace.log'))
	es = Elasticsearch(['10.24.154.234:9200'])
	# ids = es.indices.get('logstash*')
	s_log = log_str()
	print s_log
	es.indices.delete(s_log, ignore=404)
	es.indices.delete('logstash-2016.04.13', ignore=404)
	for i in es.indices.get('logstash*'):
		print i

if __name__ == '__main__':
	main()