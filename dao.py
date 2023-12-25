# Data access layer
import db_ini
import logging
import mysql.connector

db_connection = None
def connect_db() :
    global db_connection
    if not db_connection : 
        db_connection = mysql.connector.connect( **db_ini.connection_params )
    return db_connection


class Products :
    def get_all() :        
        ret = []
        sql = "SELECT * FROM products"
        try :
            db = connect_db()
            with db.cursor() as cursor :
                cursor.execute( sql )
                for row in cursor :
                    ret.append( dict( zip( cursor.column_names, map( str, row ) ) ) )
        except mysql.connector.Error as err :
            logging.error( 'SQL error', { 'sql': sql, 'err': err } )
            raise RuntimeError()
        except Exception as err :
            logging.error( 'Exception', { 'err': str( err ) } )
            raise RuntimeError()
        else :
            return ret
        
    def add( product:dict ) :
        try :
            db = connect_db()
            sql = "INSERT INTO products (`name`, `price`, `image_url`) VALUES ( %(name)s, %(price)s, %(image)s )"        
            with db.cursor() as cursor :
                cursor.execute( sql, product )
            db.commit()   # завершити транзакцію
        except mysql.connector.Error as err :
            logging.error( 'SQL error', { 'sql': sql, 'err': err } )
            raise RuntimeError()
        except Exception as err :
            logging.error( 'Exception', { 'err': str( err ) } )
            raise RuntimeError()


class Cart :
    def add( cart_item:dict ) : 
        try :
            db = connect_db()
            sql = "INSERT INTO cart (`id_user`, `id_product`, `cnt`) VALUES ( %(id_user)s, %(id_product)s, %(cnt)s )"        
            with db.cursor() as cursor :
                cursor.execute( sql, cart_item )
            db.commit()   # завершити транзакцію
        except mysql.connector.Error as err :
            logging.error( 'SQL error', { 'sql': sql, 'err': err } )
            raise RuntimeError()
        except Exception as err :
            logging.error( 'Exception', { 'err': str( err ) } )
            raise RuntimeError()


class Auth :
    def get_user_id_by_token( token:str ) -> str | None :
        # token це і є ід користувача, але перевіряємо у БД
        sql = "SELECT COUNT(u.id) FROM users u WHERE u.id=%s"
        try :
            db = connect_db()
            with db.cursor() as cursor :
                cursor.execute( sql, ( token, ) )
                cnt = cursor.fetchone()[0]
        except mysql.connector.Error as err :
            logging.error('SQL error', {'sql': sql, 'err': err})
            raise RuntimeError( str(err) )
        except Exception as err :
            logging.error('Exception', {'err': err})
            raise RuntimeError( str(err) )
        else :
            return token if cnt == 1 or cnt == "1" else None




'''
Д.З. Модифікувати метод dao.Cart.add
якщо запис з такими `id_user`, `id_product` вже є, то збільшити кількість
(cnt) замовлених одиниць. Інакше створювати новий
запис з cnt=1
'''