from datetime import datetime

from app.initial import app

from flask import jsonify, request
from sqlalchemy import select, update
from app.models import ProcessedNumbers, db
import logging


@app.route('/api/send-number/', methods=['POST'])
def send_number():
    if not request.json or 'value' not in request.json:
        return jsonify({'error': 'Incorrect request body'}), 400

    value = request.json['value']

    if not value.isdigit():
        return jsonify({'error': f'Number {value} is not in 0..N, where N - natural'}), 400

    value = int(value)
    prev_value = value - 1

    existing_number = db.session.execute(
        select(ProcessedNumbers).where(
            ProcessedNumbers.value == value
        )
    ).all()

    too_small_number = db.session.execute(
        select(ProcessedNumbers).where(
            ProcessedNumbers.value == prev_value
        )
    ).all()

    if existing_number:
        logging.error(f'Number {value} already processed')
        return jsonify({'error': f'Number {value} already processed'}), 400
    if too_small_number:
        logging.error(f'Number {value} number is one less than the processed one')
        return jsonify({'error': f'Number {value} number is one less than the processed one'}), 400

    db.session.add(ProcessedNumbers(value=value, adding_date=datetime.now()))
    db.session.commit()

    return jsonify({'success': f'{value + 1}'}), 200


