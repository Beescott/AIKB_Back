import sys, os
from flask import Blueprint, jsonify

sys.path.append('/')
sys.path.append('..')

from core import get_smartphones_query as get_smartphones_query

main = Blueprint('main', __name__)

@main.route('/add_smartphone', methods=['POST'])
def add_smartphone():
	return 'Done', 201

@main.route('/get_smartphones', methods=['GET'])
def get_smartphones():
	smartphones = get_smartphones_query.main()
	return jsonify({'smartphones': smartphones})
