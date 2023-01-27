from helpers import *

base_url = 'https://www2.correios.com.br/'
check_url = 'correios.com.br'
home_search = 'sistemas/buscacep/buscaFaixaCEP.cfm'
results_per_page = 100


class TestParser:

    def test_parse_form(self):
        from parse_data import parser
        from bs4 import BeautifulSoup

        form_page_bs, action = get_form_page(base_url, home_search, check_url)
        form = parser(form_page_bs, 'form#Geral')
        assert isinstance(
            form,
            type(BeautifulSoup('<div></div>', 'html.parser').findAll('div')))

    def test_parse_ufs(self):
        form, action = get_form_page(base_url, home_search, check_url)
        ufs = get_all_ufs(form)
        assert len(ufs) >= 27

    def test_parse_table(self):
        form, action = get_form_page(base_url, home_search, check_url)
        results, has_more_pages, header = get_results_page(
            action, {'UF': 'AC'})

        assert len(results) >= 23
        assert set(list(header)) == set(list(['UF', 'Faixa de CEP', 'Situação', 'Tipo de Faixa', 'Localidade']))
    
    def test_change_page(self):
        form, action = get_form_page(base_url, home_search, check_url)
        results, new_page, header = get_results_page(
            action, {
                'UF': 'BA',
                'Localidade': '**',
                'qtdrow': 50,
                'pagini': 50 + 1,
                'pagfim': 101
            })
        assert new_page is True
        assert len(results) >= 52