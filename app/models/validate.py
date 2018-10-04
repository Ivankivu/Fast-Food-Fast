class valid():
    def validate():

        if len(data['user_name']) == 0:
                return jsonify(
                    {"error": "username should not be empty"}), 404

        if len(data['user_email']) == 0:
                return jsonify(
                    {"error": "food should not be empty"}), 404

        if len(data['user_password']) == 0:
                return jsonify(
                    {"error": "food should not be empty"}), 404

        if data['Food'].isspace():
                return jsonify(
                    {"error": "food should not be empt spaces"}), 404

        if data['Food'].isspace():
                return jsonify(
                    {"error": "food should not be empt spaces"}), 404

        if data['Food'].isspace():
                return jsonify(
                    {"error": "food should not be empt spaces"}), 404

        if not isinstance(data['amount'], int):
                return jsonify(
                    {"error": "amount should be integer"}), 404

        if not isinstance(data['amount'], int):
                return jsonify(
                    {"error": "amount should be integer"}), 404

        if not isinstance(data['amount'], int):
                return jsonify(
                    {"error": "amount should be integer"}), 404
