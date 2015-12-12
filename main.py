import requests
import message

def GET(url_request):
    r=requests.get(url_request)
    r.status_code
    return r.text

def POST():
    return "";

def process():
    pass

#msg=message.Messsage()
req="http://tinyurl.com/api-create.php?url=http://scripting.com/"
resp=GET(req)
print resp