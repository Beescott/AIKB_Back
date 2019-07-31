from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/add_smartphone', methods=['POST'])
def add_smartphone():
	return 'Done', 201

@main.route('/get_smartphones', methods=['GET'])
def get_smartphones():

	smartphones = []
	return jsonify({'smartphones' : smartphones})