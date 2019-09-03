from SPARQLWrapper import SPARQLWrapper, JSON
import core.config as config

def main(smartphone_data):
    """
    Get all the connectivity shared between two smartphones
    """
    smartphone_names = []
    for smartphone in smartphone_data["smartphones"] :
        smartphone_names.append(smartphone["id"])
    
    sparql = SPARQLWrapper(config.graphDB_select_link)
    sparqlQuery = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX : <http://www.infotel.com/ontology/smartphone#>
        select ?connectivity where {
    """
    sparqlQuery += """
            :{} :hasConnectivity ?connectivityVersion1 .
            :{} :hasConnectivity ?connectivityVersion2 .
            ?connectivityVersion1 :versionOf ?connectivity .
            ?connectivityVersion2 :versionOf ?connectivity .
    """.format(smartphone_names[0], smartphone_names[1])
    sparqlQuery+='}'

    print(sparqlQuery)

    sparql.setQuery(sparqlQuery)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return getNamesFromQuery(results)


def getNamesFromQuery(results):
	smartphone_names = []
	for smartphone in results["results"]["bindings"]:
		smartphone_names.append(smartphone["connectivity"]["value"].split("#")[1])

	return smartphone_names
