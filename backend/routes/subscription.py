from flask import Blueprint, request, jsonify
from backend.models.database import db, Subscription

subscription_bp = Blueprint('subscription', __name__)

@subscription_bp.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        # Check if email already exists
        existing_subscription = Subscription.query.filter_by(email=email).first()
        if existing_subscription:
            return jsonify({'message': 'Email already subscribed!'}), 400

        # Save the email to the database
        new_subscription = Subscription(email=email)
        db.session.add(new_subscription)
        db.session.commit()

        return jsonify({'message': 'Subscription successful!'}), 200
    return jsonify({'error': 'Invalid email address'}), 400
