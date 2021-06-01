from broker import *

print("Welcome to Solr News Index")
print("Query types available: category, headline, short description, authors, date (format: YYYY-MM-DD) ! \n")

query_type = input("Enter query type: ")
search_word = input("Enter search word: ")
result_rows = int(input("Enter # of rows of results: "))

query_type, search_word = input_parser(query_type, search_word)

node_1, node_2, node_3 = set_urls(query_type, search_word, result_rows)

data = check_node_availaibility(node_1, node_2, node_3)

if data == "No Data Found, possible server down!":
	sys.exit()

result_rows, num_found, query_results, Qtime = check_results(data, result_rows)

print(f"\nTotal results found: {num_found}")

display(query_results)