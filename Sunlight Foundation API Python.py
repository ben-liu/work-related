# script for Sunlight Foundation API (Python)
from urllib2 import Request, urlopen, URLError

# load url in request
request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e


'''
In fact, this client/server relationship is a prerequisite of a set of principles called REST (or Representational State Transfer). This sounds kind of scary, but it's super easy—let's walk through it together.
Remember how we said HTTP involves sending hypertext (text with links)? Whenever you navigate through a site by clicking links, you're making a state transition, which brings you to the next page (representing the next state of the application). That's it!
By following this simple model of clicking from page to page, you're starting to follow REST principles. When something follows REST principles, we say that thing is RESTful. We'll cover these principles in the next exercise.

An API, or application programming interface, is kind of like a coding contract: it specifies the ways a program can interact with an application. For example, if you want to write a program that reads and analyzes data from Twitter, you'd need to use the Twitter API, which would specify the process for authentication, important URLs, classes, methods, and so on.
For an API or web service to be RESTful, it must do the following:
Separate the client from the server
Not hold state between requests (meaning that all the information necessary to respond to a request is available in each individual request; no data, or state, is held by the server from request to request)
Use HTTP and HTTP methods (as explained in the next section).
There are some other requirements, but they're beyond the scope of this lesson.

'''


from urllib2 import urlopen

kittens = urlopen('http://placekitten.com/200/300')

f = open('kittens.jpg', 'wb')
f.write(kittens.read())
f.close()


'''
Making a Request
You saw a request in the first exercise. Now it's time for you to make your own! (Don't worry, we'll help.)
On line 1, we've imported urlopen from the urllib2 module, which is the Python way of bringing in additional functionality we'll need to make our HTTP request. A module is just a collection of extra Python tools.
On line 4, we'll use urlopen on placekitten.com in preparation for our GET request, which we make when we read from the site on line 5. (On line 6, we limit the response to specific character numbers to control the input we get back—this is what gives us our cat image.)
We'll need your help to complete the request!
'''

from urllib2 import urlopen

# Open http://placekitten.com/ for reading on line 4!
kittens=urlopen("http://placekitten.com/")
response = kittens.read()
body = response[559:1000]

print body


'''
The Four Verbs
The number of HTTP methods you'll use is quite small—there are just four HTTP "verbs" you'll need to know! They are:

GET: retrieves information from the specified source.
POST: sends new information to the specified source.
PUT: updates existing information of the specified source.
DELETE: removes existing information from the specified source.
So when we sent our GET request to placekitten.com using urlopen(), we retrieved information. When you add to or update your blog, you're sending POST or PUT requests; when you delete a tweet, there goes a DELETE request.
'''

import requests
# Make a GET request here and assign the result to kittens:
kittens=requests.get("http://placekitten.com/")
print kittens.text[559:1000]


'''
An HTTP request is made up of three parts:

The request line, which tells the server what kind of request is being sent (GET, POST, etc.) and what resource it's looking for;
The header, which sends the server additional information (such as which client is making the request)
The body, which can be empty (as in a GET request) or contain data (if you're POSTing or PUTing information, that information is contained here).
'''


########## Example request #############
# POST /learn-http HTTP/1.1
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8
# Name=Eric&Age=26

import requests
body = {'Name': 'Eric', 'Age': '26'}

# Make the POST request here, passing body as the data:
response=requests.post("http://codecademy.com/learn-http/", data=body)


'''
Many APIs require an API key. Just as a real-world key allows you to access something, an API key grants you access to a particular API. Moreover, an API key identifies you to the API, which helps the API provider keep track of how their service is used and prevent unauthorized or malicious activity.

Some APIs require authentication using a protocol called OAuth. We won't get into the details, but if you've ever been redirected to a page asking for permission to link an application with your account, you've probably used OAuth.

API keys are often long alphanumeric strings. 
'''

'''
HTTP Status Codes
A successful request to the server results in a response, which is the message the server sends back to you, the client.

The response from the server will contain a three-digit status code. These codes can start with a 1, 2, 3, 4, or 5, and each set of codes means something different. (You can read the full list here). They work like this:

1xx: You won't see these a lot. The server is saying, "Got it! I'm working on your request."

2xx: These mean "okay!" The server sends these when it's successfully responding to your request.

3xx: These mean "I can do what you want, but I have to do something else first." You might see this if a website has changed addresses and you're using the old one; the server might have to reroute the request before it can get you the resource you asked for.

4xx: These mean you probably made a mistake. The most famous is "404," meaning "file not found": you asked for a resource or web page that doesn't exist.

5xx: These mean the server goofed up and can't successfully respond to your request.
'''

import requests

response = requests.get('http://placekitten.com/')

# Add your code below!
print response.status_code()


'''
The HTTP response structure mirrors that of the HTTP request. It contains:
A response line (line 2), which includes the three-digit HTTP status code;
A header line or lines (line 3), which include further information about the server and its response;
The body (line 5 and line 6), which contains the text message of the response (for example, "404" would have "file not found" in its body).
Check out the example response in the editor. See how its structure resembles the request layout?
'''

################## Example response ##########################
# HTTP/1.1 200 ok     => 200 is status code
# Content-Type: text/xml; charset=UTF-8   => more info about the server and its response

# <?xml version="1.0" encoding="utf-8"?>  => text message of the response
# <string xmlns="http://www.codecademy.com/">Accepted</string> =>200 means 'Accepted'
##############################################################

import requests
response = requests.get("http://placekitten.com/")

# print the header information from the response
print response.headers


'''
Parsing XML
XML (which stands for eXtensible Markup Language) is very similar to HTML—it uses tags between angle brackets. The difference is that XML allows you to use tags that you make up, rather than tags that the W3C decided on. For instance, you could create an API that returns information about a pet:

<pet>
  <name>Jeffrey</name>
  <species>Giraffe</species>
</pet>

As long as you document the structure of your API's response, other people can use your API to get information about <pet>s.

'''
# imported xml.dom.minidom from the xml module for parsing XML
from xml.dom import minidom

# use open() method to read from pets.txt (under the "Files") tab
f = open('pets.txt', 'r')
pets = minidom.parseString(f.read())
f.close()

names = pets.getElementsByTagName('name')
for name in names:
	print name.firstChild.nodeValue


'''
Parsing JSON
JSON (which stands for JavaScript Object Notation) is an alternative to XML. It gets its name from the fact that its data format resembles JavaScript objects, and it is often more succinct than the equivalent XML. For instance, our same <pet> Jeffrey would look like this in JSON:

{
  "pets": {
    "name": "Jeffrey",
    "species": "Giraffe"
  }
}
'''
import json
# pprint("pretty print") prints the output in a formatted way that's easier to read
from pprint import pprint

f = open('pets.txt', 'r')
pets = json.loads(f.read())
f.close()

pprint(pets)


'''
XML or JSON?
This leads us to wonder, though: how do we know whether an API will reply with XML or JSON?

The only way you'll know what type of data an API will send you is to read that API's documentation! Some will reply with one, and some will reply with the other. Documentation is a programmer's best friend, and it's always in your best interest to read it so you understand that what the API expects from you and what the API intends to send you when you make a request.
'''

### summary

# get method with urllib2
from urllib2 import urlopen
kittens=urlopen("http://placekitten.com/")
response = kittens.read()

# get method with request
response=requests.get("http://placekitten.com/")


# post method with request
import requests
body = {'Name': 'Eric', 'Age': '26'}
response=requests.post("http://codecademy.com/learn-http/", data=body)


# attributes of requests.get
response = requests.get("http://placekitten.com/")

response.headers	
response.status_code()	
response.json
response.url


# capitol words API

'''

'''

import requests
import pprint

# filters on endpoint data
query_params = { 'apikey': 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
             'phrase': 'fiscal cliff'}
# determines what type of data you will get back
endpoint = 'http://capitolwords.org/api/text.json'  
response = requests.get( endpoint, params=query_params)
data = response.json
pprint.pprint(data)

#request_url ?
request_url=response.url
print request_url


# capitol words API practise
import requests
import pprint

query_params = { 'apikey': 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
         'per_page': 3,
            'phrase': 'holiday season',
            'start_date': '2012-11-01',
            'end_date': '2012-12-31'
        }

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get(endpoint, params=query_params)

data = response.json
pprint.pprint(data)


# manipulate results
import requests
import pprint

query_params = { 'apikey': 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
             'per_page': 3,
             'phrase':'happy holidays',
             'sort':'date desc'
            }

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get(endpoint, params=query_params)
data = response.json
legislator = data['results'][0]['speaker_first']+" "+data['results'][0]['speaker_last']
date = data['results'][0]['date']

print "%s said happy holidays on %s" % (legislator,date)


# build API interface



