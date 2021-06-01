import urllib.parse
import requests
import sys

def check_results(data, result_rows):
	if data['response']['numFound'] == 0:
		return 0, 0, 0, 0

	if data['response']['numFound'] < result_rows:
		result_rows = data['response']['numFound']

	return result_rows, data['response']['numFound'], data['response']['docs'], data['responseHeader']['QTime']

def input_parser(query_type, search_word):

	if query_type == "date":
		search_word = "[" + search_word + "T00:00:00Z TO " + search_word + "T00:00:00Z" + "]"
	if query_type == "short description":
		query_type = query_type.replace(" ", "_")

	search_word = search_word.replace(" ", "%20")
	search_word = search_word.replace("\"", "%22")
	search_word = search_word.replace("[", "%5B")
	search_word = search_word.replace("]", "%5D")

	return query_type, search_word

def set_urls(query_type, search_word, result_rows):

	node_1 = f"http://localhost:8983/solr/news/select?q={query_type}%3A{search_word}&rows={result_rows}"
	node_2 = f"http://localhost:8984/solr/news/select?q={query_type}%3A{search_word}&rows={result_rows}"
	node_3 = f"http://localhost:8985/solr/news/select?q={query_type}%3A{search_word}&rows={result_rows}"

	return node_1, node_2, node_3

def check_node_availaibility(node_1, node_2, node_3):

	try:
		response = requests.get(node_1).json()
	except ConnectionError:
		try:
			response = requests.get(node_2).json()
		except ConnectionError:
			try:
				response = requests.get(node_3).json()
			except ConnectionError:
				return "No Data Found, possible server down!"	

	return response

def display(data):
	print()
	for i in range(len(data)):
		try:
			print("Category: " + str(data[i]['category']))
		except KeyError:
			print("Category not available")

		try:
			print(f"Headline: " + str(data[i]['headline']))
		except KeyError:
			print("Headline not available")

		try:
			print(f"Authors: " + str(data[i]['authors']))
		except KeyError:
			print("Authors not available")
		
		try:
			print(f"Link: " + str(data[i]['link']))
		except KeyError:
			print("Link not available")
		
		try:
			print(f"Short Description: " + str(data[i]['short_description']))
		except KeyError:
			print("Short Description not available")
		
		try:
			print(f"Date: " + str(data[i]['date']))
		except KeyError:
			print("Date not available")
		print()