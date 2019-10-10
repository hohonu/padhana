import os

from padhana.analysis import TextLayoutAnalysis, OutlineAnalysis
from padhana.parsers import PdfMinerParser


def get_test_directory():
    return os.path.dirname(os.path.abspath(__file__)) + "/../test_documents/"


def get_text_layout_analysis(filename):
    parser = PdfMinerParser()
    document = parser.parse_file(str(get_test_directory()) + filename + '.pdf')
    text_layout_analysis = TextLayoutAnalysis(document)
    return text_layout_analysis


def print_page_details(page):
    print("--------------------------------- NEW PAGE --------------------------------")
    for content_area in page.content_areas:
        print("--------------------------------- CONTENT AREA --------------------------------- ")
        if content_area.features.image_node:
            print('This content area has an image')
            print(content_area.features.image_node.node)
            print('*********************\n\n')
        for line in content_area.lines:
            print(line.as_string())
        print('\n\n')


def test_prospectus():
    filename = 'FRS189 Pricing Supplement 20190301'
    text_layout_analysis = get_text_layout_analysis(filename)

    page_index_list = range(0,2)
    for page_index in page_index_list:
        page = text_layout_analysis.pages[page_index]
        print_page_details(page)
