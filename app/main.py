from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from code import broker

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/news")
async def root(request: Request):
	return templates.TemplateResponse("home.html", context={"request": request})

@app.post("/news")
async def search_query(request: Request, query_type: str = Form(...), search_word: str = Form(...), result_rows: int = Form(...)):

	query = {"query_type": query_type, "search_word": search_word, "result_rows": result_rows}

	query_type, search_word = broker.input_parser(query_type, search_word)
	node_1, node_2, node_3 = broker.set_urls(query_type, search_word, result_rows)
	data = broker.check_node_availaibility(node_1, node_2, node_3)
	result_rows, num_results, query_results, Qtime = broker.check_results(data, result_rows)

	if query_results == 0:
		return templates.TemplateResponse("home.html", context = {"request": request, "num_results": num_results, "query_results": query_results, "query": query, "Qtime": Qtime})

	query["result_rows"] = result_rows

	return templates.TemplateResponse("home.html", context = {"request": request, "num_results": num_results,"query_results": query_results, "query": query, "Qtime": Qtime})