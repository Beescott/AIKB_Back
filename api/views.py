import sys, os
from flask import Blueprint, jsonify, request
import core.GraphDBRequests.SmartphoneRequest as SmartphoneRequest

sys.path.append('/')
sys.path.append('..')

from core import get_smartphones_query as get_smartphones_query
from core import get_smartphones_from_search as get_smartphones_from_search
from core import insert_latest_smartphones as insert_latest_smartphones
from core import get_compatible_smartphones as get_compatible_smartphones
from core import get_connectivity_from_smartphones_query as get_connectivity_from_smartphones_query
from core.Smartphone import Smartphone

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return "Hello!"

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

@main.route('/insert_smartphones', methods=['POST'])
def insert_smartphones():
	insert_latest_smartphones.main()
	return 'Done'

@main.route('/get_compatible_smartphones_with_system', methods=['POST'])
def get_compatible_smartphones_with_system():
	smartphones_data = request.get_json()
	smartphones = get_compatible_smartphones.main(smartphones_data)
	return jsonify({'smartphones': smartphones})

@main.route('/post_new_smartphone', methods=['POST'])
def post_new_smartphone():
	smartphone_data = request.get_json()['smartphone']
	smartphone = Smartphone(smartphone_data['name'])
	smartphone.format(smartphone_data)
	smartphone.format_version()
	smartphone.display()
	SmartphoneRequest.insert_phone(smartphone)
	return "Done"

@main.route('/get_connectivity_from_smartphones', methods=['POST'])
def get_connectivity_from_smartphones():
	smartphones_data = request.get_json()
	connectivities = get_connectivity_from_smartphones_query.main(smartphones_data)
	return jsonify({'connectivities': connectivities})
