#!C:\Python312\python.exe

import os

# сформувати з змінних перелік <ul> name = value
# envs = os.environ  # змінні оточення -- dict{ name: value }
envs = f"<ul>{"".join([f"<li>{k} = {v}</li>" for k,v in os.environ.items()])}</ul>"

print( "Content-Type: text/html; charset=cp1251" )
print( "Connection: close" )
print()   # порожній рядок - кінець заголовків
print( f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="cp1251">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGI</title>
</head>
<body>
    <h1>CGI працює</h1>
    <p>{envs}</p>
</body>
</html>''' )


"""
Д.З. CGI: забезпечити відображення лише наступних змінних оточення
REQUEST_URI, QUERY_STRING, REQUEST_METHOD, REMOTE_ADDR, REQUEST_SCHEME 
Розібрати рядок QUERY_STRING у словник 
 x=10&y=20  --> {x: 10, y: 20}
"""