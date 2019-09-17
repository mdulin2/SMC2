'''
To get going: 
- Use the virtualenv to install Flask 
- python redirect_fun.py
- python flag.py

Valid redirect: http://localhost:8000/?page=/you_were_redirected 
Invalid redirect: http://localhost:8000/?page=you_were_redirected
Redirect (win): http://localhost:8000/?page=//127.0.0.1
Redirect (win): http://localhost:8000/?page=http://127.0.0.1
'''

from flask import Flask, redirect, request, Response
import re

app = Flask(__name__)

@app.route("/")
def index():
    page = request.args.get('page')
    bypass = verify(page)
    if(bypass == True):
        value = "{Flag}"
        headers={'Location': page + "?page=" + value }

    else:
        value = ""
        headers={'Location': page }

    if(bypass == False and page[0] == '/'):
        return Response(page, status=302, headers=headers)

    print(page + "?" + value)
    if(bypass == False):
        return "Bad redirect... Not a valid URL for this"
    return Response(page, status=302, headers=headers)

def verify(page):
    # Found this regex at: https://www.regexpal.com/93652
    # The second version allows for //domain or an ip. 
    print("Page: ", page)
    is_url = re.search('^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$', page) 
    
    if(page[0] == "/" and page[1] == "/"):
        print("Super Bypass Attempted")
        return False 
    elif(is_url  == None):
        if(re.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', page[7:]) != None):
            print("IP Address")
            return True 
        print("Not URL")
        return False 
    
    else:
        print("Full URL") 
        return False
 
@app.route("/you_were_redirected")
def redirected():
    return "You were redirected. Congrats :)!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000,debug=True)
