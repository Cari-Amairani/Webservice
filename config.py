import web

db_host = 'localhost'
db_name = 'ferre_cadr'
db_user = 'cadr'
db_pw = 'cadr.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )