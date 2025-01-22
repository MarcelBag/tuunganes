from flask import Blueprint, request, jsonify

# adding a blueprint for sub
subscription_bp = Blueprint('subscription', __name__)

# Route to handle email subscriptions
@subscription_bp.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        # Save email to a file (replace with a database later)
        with open('subscribers.txt', 'a') as f:
            f.write(email + '\n')
        return jsonify({'message': 'Subscription successful!'}), 200
    return jsonify({'error': 'Invalid email address'}), 400
