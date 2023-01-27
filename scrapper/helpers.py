import pandas as pd

from parse_data import parser
from request_data import requester


def get_all_ufs(form_page_bs):
    """ This function gets the form page response
    and parse it to get the possible values
    for the POST request to be done later"""
    collection_ufs = parser(form_page_bs, 'select option')
    return [ufs['value'] for ufs in collection_ufs if ufs['value'] != '']


def get_form_page(base_url, home_search, check_url):
    """This function gets the url and returns the form action
    and the form bs element"""
    form_page_bs = requester(base_url + home_search)
    form = parser(form_page_bs, 'form#Geral')
    action = base_url + form[0]['action'] if check_url not in form[0][
        'action'] else form[0]['action']
    return form_page_bs, action


def get_results_page(action, payload):
    """This function provides a helper to not only
    get the header (we evaluate the header in a response basis)
    but also to evaluate if there are other pages in the result set"""
    result_page_bs = requester(action, 'POST', data=payload)
    results = parser(result_page_bs, '.laminas table')
    header = []
    if results:
        header = [s.text for s in results[-1].select('tr th')
                  ]  # Now only getting the header
        results = results[-1].findAll('tr')  # Getting all rows
        header.append(
            'UF')  # Here we add the column UF to better categorize the data
    has_more_pages = bool(
        len(
            parser(
                result_page_bs,
                'a[href="javascript:document.Proxima.submit(\'Proxima\')"]')))
    return results, has_more_pages, header


def parse_results(result):
    """ This function gets the text from the columns """
    allColumns = [s.text for s in result.findAll('td')]
    return allColumns


def dump_jsonl(resultDict=[{}], path='result.jsonl'):
    """This function writes the final file. 
    Beware, the file will be replaced"""
    df = pd.DataFrame(resultDict)
    df['ID'] = df.index + 1
    df = df.drop_duplicates(['UF', 'Localidade', 'Faixa de CEP'], keep='first')
    with open(path, 'w', encoding='utf-8') as file:
        df.to_json(path,
                   lines=True,
                   orient='records',
                   index=True,
                   force_ascii=False)