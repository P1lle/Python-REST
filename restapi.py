from flask import Flask
from flask import request
import uuid

app = Flask('Wichbois')

todolists=[]

class todolist:
    name = ''
    id = 1
    items = []


@app.route('/todo-list/<list_id>', methods=['GET','DELETE'])
def todolistID(list_id):
    if request.method == 'DELETE':
        if list_id not in todolists :
            return 'fehlerhafte ID', 404
        else :
            del todolists[list_id]
            return 'OK', 200
    if request.method == 'GET' : 
        if list_id in todolists :
            return todolists[list_id]
        else :
            return 'fehlerhafte ID', 404
        

@app.route('/todo-list', methods=['POST'])
def todolist():
    if request.form.get('name') is not None :
        uui = uuid.uuid4()
        todolists.update({'list_id':uui,
                        'name':request.form.get('name')})
        return todolists[uui], 200
    

@app.route('/todo-list/<list_id>/entry', methods=['POST'])
def entry(list_id):
    if request.form.get('name') is not None and request.form.get('beschreibung') is not None and request.args.get('list_id'):
        todolists.update({'list_id':list_id,
                        'name':request.form.get('name'),
                        'beschreibung':request.form.get('beschreibung')})
        return todolists[todolists.index(list_id)], 200

@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['PUT'])
def put(list_id,entry_id):
    todolists[todolists.index(list_id)].beschreibung = request.args.get('beschreibung')
    todolists[todolists.index(list_id)].name = request.args.get('name')
    return todolists[todolists.index(list_id)],200

@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['DELETE'])
def delete(list_id,entry_id):
    if todolists[todolists.index(list_id)] is not None:
        todolists[todolists.index(list_id)].remove()
        return 200
    return 404

        

app.run(host='0.0.0.0', port = 5000)