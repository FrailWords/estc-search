from bs4 import BeautifulSoup
from functools import partial
import urllib.request
from urllib.parse import parse_qs, urlencode, urlsplit

columns = ["ESTC No.", "Title", "Author", "Publisher Info", "Description", "Locations", "General Notes", "Citation/Ref. Notes", "Electronic Location"]
text_queries = ["ESTC Citation No.", "Main Title", "ME-Personal Name", "Imprint", "Phys.Description", "Location",
                "General Note", "Citation/Ref. Note", "Electronic Location"]


def _query_html(soup: BeautifulSoup, field: str) -> str:
    # find all values containing query field
    all_text = soup.find_all('td', string=field)
    values = []
    for text in all_text:
        value = text.find_next_sibling("td").text.strip()
        if value is not None and value != 'nan':
            value = value.replace('\xa0', ' ')
            values.append(value)
        else:
            values.append('')
    return '\t---\t'.join(values)


def _read_url(url: str):
    fp = urllib.request.urlopen(url)
    url_bytes = fp.read()

    html_string = url_bytes.decode("utf8")
    fp.close()
    return html_string


def _estc_url(estc_number: str):
    print("Fetching information for ESTC number:", estc_number)
    url = "http://estc.bl.uk/{}".format(estc_number)
    html = _read_url(url)
    soup = BeautifulSoup(html, 'html.parser')
    el = soup.select_one("a[href*=set_entry]")
    href = el.get('href')
    parsed = urlsplit(href)
    query_dict = parse_qs(parsed.query)
    query_dict['format'][0] = '002'
    query_new = urlencode(query_dict, doseq=True)
    parsed = parsed._replace(query=query_new)
    url_new = (parsed.geturl())
    return url_new


def _est_info_for_number(estc_number: str) -> []:
    url = _estc_url(estc_number)
    html = _read_url(url)
    # text_file = open("test.html", "r")
    # html = text_file.read()
    soup = BeautifulSoup(html, "html.parser")
    _do_query = partial(_query_html, soup)

    df_values = []
    for column, query in zip(columns, text_queries):
        df_values.append(_do_query(query))
    return df_values


def est_info(estc_numbers: [str]) -> [object]:
    result = [columns]
    for estc_number in estc_numbers:
        result.append(_est_info_for_number(estc_number))
    return result
