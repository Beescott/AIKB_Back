from SPARQLWrapper import SPARQLWrapper, JSON
import core.config as config

def main(smartphones_data):
    print(smartphones_data)
    sparql = SPARQLWrapper(config.graphDB_select_link)
    sparqlQuery = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX : <http://www.infotel.com/ontology/smartphone#>
        select ?compatible_smartphone_name ?id where {
    """

    for smartphone in smartphones_data["smartphones"]:
        sparqlQuery += """
            :{} :canConnectTo ?compatible_smartphone .
        """.format(smartphone["id"])
    
    sparqlQuery += """
            ?compatible_smartphone :Device_name ?compatible_smartphone_name .
            ?compatible_smartphone :deviceId ?id
        }
    """

    sparql.setQuery(sparqlQuery)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return getNamesFromQuery(results)

def getNamesFromQuery(results):
	smartphone_names = []
	for smartphone in results["results"]["bindings"]:
		smartphone_names.append({
            "name":smartphone["compatible_smartphone_name"]["value"],
            "id":smartphone["id"]["value"]
        })

	return smartphone_names
