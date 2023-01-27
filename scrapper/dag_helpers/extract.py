import argparse
import os

from helpers import *

base_url = 'https://www2.correios.com.br/'
check_url = 'correios.com.br'
home_search = 'sistemas/buscacep/buscaFaixaCEP.cfm'
results_per_page = 50  # Default from the network calls


def extract(ufs=[]):
    """This function takes advantage of the functions created
    in the helpers file to process the data and store it"""
    print('Starting the crawler...')
    form_page, action = get_form_page(base_url, home_search, check_url)
    if not ufs:
        ufs = get_all_ufs(form_page)
    print("We are going to extract the following list of UFs: ")
    print(ufs, sep="\n")
    dump = []
    for uf in ufs:
        print("Extracting " + uf)
        results, new_page, header = get_results_page(action, {
            'UF': uf,
            'Localidade': ''
        })
        nresults = len(results)
        while True:
            columns = parse_results(results[-1])
            if len(columns) > 0:
                columns.append(uf)
                dump.append(dict(zip(header, columns)))
            del results[-1]
            if new_page and len(results) == 0:
                # We are out of rows, let's fetch more if possible
                results, new_page, header = get_results_page(
                    action, {
                        'UF': uf,
                        'Localidade': '**',
                        'qtdrow': results_per_page,
                        'pagini': nresults + 1,
                        'pagfim': nresults + results_per_page
                    })
                # Pagination strategy used by the website POST method
                nresults += len(results)
            if len(results) == 0:
                break

        print("Done")
    dump_jsonl(dump, 'result.jsonl')