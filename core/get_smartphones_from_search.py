from SPARQLWrapper import SPARQLWrapper, JSON
import core.config as config

def main(smartphone_data):
    first_letters = smartphone_data["name"]
    first_letters = "one"
    sparql = SPARQLWrapper(config.graphDB_select_link)
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX : <http://www.infotel.com/ontology/smartphone#>
        select ?name where {
            ?s rdf:type :Smartphone .
            ?s :Device_name ?name .
            FILTER regex(?name, '"""+first_letters+"""', "i")
        } limit 100
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return getNamesFromQuery(results)


def getNamesFromQuery(results):
	smartphone_names = []
	for smartphone in results["results"]["bindings"]:
		smartphone_names.append(smartphone["name"]["value"])

	return smartphone_names
