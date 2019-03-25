import web
import config

db = config.db


def get_all_clientes():
    try:
        return db.select('clientes')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_clientes(id):
    try:
        return db.select('clientes', where='id=$id', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_clientes(id):
    try:
        return db.delete('clientes', where='id=$id', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_clientes(nombre,ape_mat,ape_pat,telefono,correo):
    try:
        return db.insert('clientes',nombre=nombre,
ape_mat=ape_mat,
ape_pat=ape_pat,
telefono=telefono,
correo=correo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_clientes(id,nombre,ape_mat,ape_pat,telefono,correo):
    try:
        return db.update('clientes',id=id,
nombre=nombre,
ape_mat=ape_mat,
ape_pat=ape_pat,
telefono=telefono,
correo=correo,
                  where='id=$id',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
