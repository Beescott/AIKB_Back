from SPARQLWrapper import SPARQLWrapper, JSON
import core.config as config


def insert_phone(formated_phone):
    """
        Insert a smartphone inside GraphDB
    :param formated_phone:
    :return:
    """
    insert_query_string = """
        PREFIX : """ + config.file_prefix + """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        INSERT DATA {
    """

    phone_name_sql = formated_phone.name.replace(" ", "").lower()
    # Replace the () by _ and nothing, example : apple ipad air (2019) = appleipadair_2019
    phone_name_sql = phone_name_sql.replace('(', '_').replace(')', '')
    insert_query_string += ':{} rdf:type :Smartphone '.format(phone_name_sql) + '.\n'

    # Add the name of the smartphone
    insert_query_string += ':{} :Device_name "{}"'.format(phone_name_sql, formated_phone.name) + ' .\n'
    insert_query_string += ':{} :deviceId "{}"'.format(phone_name_sql, phone_name_sql) + ' .\n'

    for information in formated_phone.formated_connectivities:
        # if the device has the connectivity
        if formated_phone.formated_connectivities[information] != 'No':
            if information in formated_phone.formated_version:
                insert_query_string += ':{} rdf:type :{} .\n'.format(
                    formated_phone.formated_version[information], information)
                insert_query_string += ':{} :versionOf :{} .\n'.format(
                    formated_phone.formated_version[information], information)
                insert_query_string += ':{} :versionName "{}" .\n'.format(
                    formated_phone.formated_version[information],
                    formated_phone.formated_connectivities[information]
                )
                insert_query_string += ':{} :hasConnectivity :{} . \n'.format(phone_name_sql,
                                                                         formated_phone.formated_version[
                                                                             information])
            else:
                insert_query_string += ':{} :hasConnectivity :{} . \n'.format(phone_name_sql, information)

    insert_query_string += '}'

    print(insert_query_string)

    sparql_insert_wrapper = config.graphDB_insert_link

    sparql = SPARQLWrapper(sparql_insert_wrapper)

    sparql.method = 'POST'
    sparql.setQuery(insert_query_string)
    sparql.query()
