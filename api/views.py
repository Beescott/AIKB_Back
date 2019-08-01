import sys, os
from flask import Blueprint, jsonify, request

sys.path.append('/')
sys.path.append('..')

from core import get_smartphones_query as get_smartphones_query
from core import get_smartphones_from_search as get_smartphones_from_search

main = Blueprint('main', __name__)

@main.route('/add_smartphone', methods=['POST'])
def add_smartphone():
	return 'Done', 201

@main.route('/get_smartphones', methods=['GET'])
def get_smartphones():
	smartphones = get_smartphones_query.main()
	return jsonify({'smartphones': smartphones})

@main.route('/get_smartphones_from_field', methods=['POST'])
def get_smartphones_from_field():
	smartphone_data = request.get_json()
	smartphones = get_smartphones_from_search.main(smartphone_data)
	return jsonify({'smartphones': smartphones})
