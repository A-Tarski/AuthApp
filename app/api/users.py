from flask import jsonify, request, g, abort
from app import db
from app.models import User
from app.api import bp
from app.api.auth import basic_auth, error_response


# TODO add view for getting session token
# TODO header={'Set-Cookie': 'token=session_token'}

@bp.route('/users/<int:id>', methods=['GET'])
@basic_auth.login_required
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['GET'])
@basic_auth.login_required
def get_users():
    return jsonify([user.to_dict() for user in User.query.all()])


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return error_response(400, 'Wrong registration data or not all data was send')
    if User.query.filter_by(email=data['email']).first() or \
            User.query.filter_by(username=data['username']).first():
        return error_response(400, 'Try another registration data')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    return response


@bp.route('/users/<int:id>', methods=['PUT'])
@basic_auth.login_required
def update_user(id):
    if g.current_user.id != id:
        abort(403)
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        return error_response(400, 'please use a different username')
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first():
        return error_response(400, 'please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users/<int:id>', methods=['DELETE'])
@basic_auth.login_required
def delete_user(id):
    if g.current_user.id != id:
        abort(403)
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    response = jsonify({'message': 'Success deleted'})
    response.status_code = 200
    return response