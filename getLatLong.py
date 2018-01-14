import httplib2;
import json;
import sys;
import codecs;

sys.stdout = codecs.getwriter('utf8')(sys.stdout);
sys.stderr = codecs.getwriter('utf8')(sys.stderr);

myGoogleMapApiKey = 'AIzaSyAQQ51ldMB99t_REnSqxSdhVV9v6QRaDD8';

def getLatLong(inputAddress):
	address = inputAddress.replace(' ','+');
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(address,myGoogleMapApiKey));
	h = httplib2.Http();
	result = json.loads(h.request(url,'GET')[1]);
	lattitude = result['results'][0]['geometry']['location']['lat'];
	longitude = result['results'][0]['geometry']['location']['lng'];
	return (str(lattitude),str(longitude))



