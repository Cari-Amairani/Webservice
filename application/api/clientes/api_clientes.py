import web
import config
import json


class Api_clientes:
    def get(self, id):
        try:
            # localhost:8080/api_clientes?user_hash=12345&action=get
            if id is None:
                result = config.model.get_all_clientes()
                clientes_json = []
                for row in result:
                    tmp = dict(row)
                    clientes_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
            else:
                # localhost:8080/api_clientes?user_hash=12345&action=get&id=1
                result = config.model.get_clientes(int(id))
                clientes_json = []
                clientes_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

# localhost:8080/api_clientes?user_hash=12345&action=put&id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,ape_mat,ape_pat,telefono,correo):
        try:
            config.model.insert_clientes(nombre,ape_mat,ape_pat,telefono,correo)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# localhost:8080/api_clientes?user_hash=12345&action=delete&id=1
    def delete(self, id):
        try:
            config.model.delete_clientes(id)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# localhost:8080/api_clientes?user_hash=12345&action=update&id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id, nombre,ape_mat,ape_pat,telefono,correo):
        try:
            config.model.edit_clientes(id,nombre,ape_mat,ape_pat,telefono,correo)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id=None,
            nombre=None,
            ape_mat=None,
            ape_pat=None,
            telefono=None,
            correo=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id=user_data.id
            nombre=user_data.nombre
            ape_mat=user_data.ape_mat
            ape_pat=user_data.ape_pat
            telefono=user_data.telefono
            correo=user_data.correo
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id)
                elif action == 'put':
                    return self.put(nombre,ape_mat,ape_pat,telefono,correo)
                elif action == 'delete':
                    return self.delete(id)
                elif action == 'update':
                    return self.update(id, nombre,ape_mat,ape_pat,telefono,correo)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
