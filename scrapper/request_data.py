import requests


def requester(
        url,
        method='GET',
        header={
            'Origin':
            'https://www2.correios.com.br',
            'Referer':
            'https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        },
        data={},
        default_timeout=5):
    """This function implements requests
    with a default header and fetches data from url"""
    if method == 'GET':
        request = requests.get(url, headers=header, timeout=default_timeout)
    if method == 'POST':
        request = requests.post(url,
                                headers=header,
                                data=data,
                                timeout=default_timeout)

    return request
