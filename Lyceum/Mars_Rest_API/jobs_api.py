import flask
from flask import jsonify, request
from data import db_session
from data.jobs import Jobs
import datetime

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    j = session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                 for item in j]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>',  methods=['GET'])
def get_one_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': job.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    if request.json.get('id'):
        if session.query(Jobs).filter(Jobs.id == int(request.json['id'])).first():
            return jsonify({'error': 'Id already exists'})
    try:
        job = Jobs(
            team_leader=int(request.json['team_leader']),
            job=request.json['job'],
            work_size=int(request.json['work_size']),
            collaborators=request.json['collaborators'],
            start_date=datetime.datetime.strptime(
                request.json['start_date'], '%d-%m-%y').date(),
            is_finished=request.json['is_finished']
        )
        if request.json.get('id'):
            job.id = int(request.json['id'])
        if request.json.get('end_date'):
            job.end_date = datetime.datetime.strptime(
                request.json['end_date'], '%d-%m-%y').date()
        session.add(job)
        session.commit()
    except Exception:
        return jsonify({'error': 'Convert value Error'})

    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': f'Id <{job_id}> not found'})
    session.delete(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs', methods=['PUT'])
def update_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    elif not type(request.json['id']) == int:
        return jsonify({'error': 'Id not int()'})

    session = db_session.create_session()
    job = session.query(Jobs).filter(
        Jobs.id == int(request.json['id'])).first()
    if not job:
        return jsonify({'error': f'Id <{request.json["id"]}> not found'})
    try:
        job.team_leader = int(request.json['team_leader'])
        job.job = request.json['job']
        job.work_size = int(request.json['work_size'])
        job.collaborators = request.json['collaborators']
        job.start_date = datetime.datetime.strptime(
            request.json['start_date'], '%d-%m-%y').date()
        job.is_finished = request.json['is_finished']
        if request.json.get('end_date'):
            job.end_date = datetime.datetime.strptime(
                request.json['end_date'], '%d-%m-%y').date()

    except Exception:
        return jsonify({'error': 'Convert value Error'})
    session.commit()

    return jsonify({'success': 'OK'})
