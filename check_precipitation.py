import urllib2
import urllib
from xml.etree import ElementTree as ET

params = {
    'lat': 31.971059,
    'lon': -112.805214,
    'product': 'time-series',
    'begin': '2004-04-27T12:00',
    'qpf': 'qpf'
}

base_url = 'http://www.weather.gov/forecasts/xml/sample_products/browser_interface/ndfdXMLclient.php'
query_url = base_url + "?" + urllib.urlencode(params)
res = urllib2.urlopen(query_url, " ")
content = res.read()

e = ET.fromstring(content)

start_times = []
end_times = []
precip_inches = []

for node in e.getiterator():
    if node.tag == 'start-valid-time':
        start_times.append(node.text)
    elif node.tag == 'end-valid-time':
        end_times.append(node.text)
    elif node.tag == 'value':
        precip_inches.append(node.text)
