#!C:\Python312\python.exe

import os

# сформувати з змінних перелік <ul> name = value
# envs = os.environ  # змінні оточення -- dict{ name: value }
envs = f"<ul>{"".join([f"<li>{k} = {v}</li>" for k,v in os.environ.items()])}</ul>"

print( "Content-Type: text/html; charset=cp1251" )
print( "Connection: close" )
print()   # порожній рядок - кінець заголовків
with open( 'home.html' ) as file :
    print( file.read() )


"""
Д.З. CGI: забезпечити відображення лише наступних змінних оточення
REQUEST_URI, QUERY_STRING, REQUEST_METHOD, REMOTE_ADDR, REQUEST_SCHEME 
Розібрати рядок QUERY_STRING у словник 
 x=10&y=20  --> {x: 10, y: 20}
"""