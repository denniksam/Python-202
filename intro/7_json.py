# Робота з даними у форматі JSON
import json  # входить у базовий комплект Python

def create_json_file() -> None :
    try :
        with open( "data.json", mode="w", encoding="utf-8" ) as file :
            file.write( '''{
                       "str": "Hello, World",
                       "digital": 1213,
                       "float": 1.456,
                       "bool1": true,
                       "null": null,
                       "obj": {
                            "bool0": false,
                            "str": "A string"
                       },
                       "arr": [1,2,3,4,5]
            }''' )
    except IOError as err :
        print( err )
    else :
        print( "create_json_file OK" )


def print_json() :
    try :
        with open("data.json") as file :
            j = json.load( file )
        print( type(j), j )  # <class 'dict'> {'str': 
        for k in j :
            print( k, j[k], type(j[k]) )
        j['cyr'] = "Кирилічні дані"
        print( '===========================' )
        print( j )              # ... 'cyr': 'Кирилічні дані'
        print( json.dumps(j) )  # ... "cyr": "\u041a\u0438\u0440\u04
        print( json.dumps( j,   # ... "cyr": "Кирилічні дані"
            ensure_ascii=False, # Unescaped unicode
            indent=2 ) )        # Pretty print (2 spaces)
    except :
        print( "Error" )


def main() -> None :
    # create_json_file()
    print_json()


if __name__ == "__main__" :
    main()
