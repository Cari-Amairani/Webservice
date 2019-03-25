import config
import hashlib
import app

class Edit:

    def __init__(self):
        pass

    def GET(self, id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    def GET_EDIT(id, **k):
        message = None # Error message
        id = config.check_secure_val(str(id)) # HMAC id validate
        result = config.model.get_clientes(int(id)) # search for the id
        result.id = config.make_secure_val(str(result.id)) # apply HMAC for id
        return config.render.edit(result, message) # render clientes edit.html

    def POST_EDIT(id, **k):
        form = config.web.input()  # get form data
        form['id'] = config.check_secure_val(str(form['id'])) # HMAC id validate
        # edit user with new data
        result = config.model.edit_clientes(
            form['id'],form['nombre'],form['ape_pat'],form['ape_mat'],form['telefono'],form['correo'],
        )
        if result == None: # Error on udpate data
            id = config.check_secure_val(str(id)) # validate HMAC id
            result = config.model.get_clientes(int(id)) # search for id data
            result.id = config.make_secure_val(str(result.id)) # apply HMAC to id
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/clientes') # render clientes index.html
