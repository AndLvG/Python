import flask
from flask import jsonify, request
from data import db_session
from data.users import User
import datetime

blueprint = flask.Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/api/users')
def get_users():
    session = db_session.create_session()
    j = session.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id','surname','name','age','position','speciality','address','email'))
                 for item in j]
        }
    )


@blueprint.route('/api/users/<int:user_id>',  methods=['GET'])
def get_one_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'users': user.to_dict(only=('id','surname','name','age','position','speciality','address','email'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname','name','age','position','speciality','address','email','password']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    try:
        user = User(
            surname=request.json['surname'],
            name=request.json['name'],
            age=int(request.json['age']),
            position=request.json['position'],
            speciality=request.json['speciality'],
            address=request.json['address'],
            email=request.json['email']
        )
        user.set_password(request.json['password'])
        session.add(user)
        session.commit()
    except Exception:
        return jsonify({'error': 'Convert value Error'})

    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': f'Id <{user_id}> not found'})
    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users', methods=['PUT'])
def update_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id','surname','name','age','position','speciality','address','email']):
        return jsonify({'error': 'Bad request'})
    elif not type(request.json['id']) == int:
        return jsonify({'error': 'Id not int()'})

    session = db_session.create_session()
    user = session.query(User).filter(
        user.id == int(request.json['id'])).first()
    if not user:
        return jsonify({'error': f'Id <{request.json["id"]}> not found'})
    try:
        user.surname=request.json['surname'],
        user.name=request.json['name'],
        user.age=int(request.json['age']),
        user.position=request.json['position'],
        user.speciality=request.json['speciality'],
        user.address=request.json['address'],
        user.email=request.json['email']
      
        session.commit()
    
    except Exception:
        return jsonify({'error': 'Convert value Error'})
    session.commit()

    return jsonify({'success': 'OK'})
