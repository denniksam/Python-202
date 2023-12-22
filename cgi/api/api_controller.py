import json
import mysql.connector
import os
import sys
sys.path.append( '../' )
import db_ini

class ApiController :

    def __init__( self ) -> None:
        self.db_connection = None

    def serve( self ) -> None :
        '''Основний метод оброблення запиту з розглажунням
        у відповідності до НТТР-методу'''
        
        method = os.environ.get( 'REQUEST_METHOD', '' )   # "GET"
        action = f"do_{method.lower()}"                   # "do_get"
        attr = getattr( self, action, None )              # obj.do_get
        if attr is None :
            self.send_response( 405, "Method Not Allowed", 
                               { "message": f"Method '{method}' not allowed" } )
        else :
            attr()

    def send_response( self, 
                      status_code:int=200, 
                      reason_phrase:str="OK", 
                      body:object=None,
                      data:object=None,
                      meta:object=None ) -> None :
        status_header = f"Status: {status_code} {reason_phrase if reason_phrase else ''}"
        print( status_header )    
        print( "Content-Type: application/json" )
        print( "Connection: close" )
        print()   # порожній рядок - кінець заголовків
        if body :
            print( json.dumps( body ), end='' )
        else :
            print( json.dumps( { "meta": meta, "data": data } ), end='' )
        exit()
    
    def connect_db_or_exit( self ) :
        if not self.db_connection :        
            try :
                self.db_connection = mysql.connector.connect( **db_ini.connection_params )
            except mysql.connector.Error as err :
                self.send_response( 500, "Internal Server Error", str(err) )   # TODO: прибрати str(err) 
        return self.db_connection
