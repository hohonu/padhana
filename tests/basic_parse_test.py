import os

from padhana.analysis import TextLayoutAnalysis, LineLayoutAnalysis
from padhana.parsers import PdfMinerParser


def get_test_directory():
    return os.path.dirname(os.path.abspath(__file__)) + "/../test_documents/"


def get_text_layout_analysis(filename):
    parser = PdfMinerParser()
    document = parser.parse_file(str(get_test_directory()) + filename + '.pdf')
    text_layout_analysis = TextLayoutAnalysis(document)
    return text_layout_analysis


def get_line_layout_analysis(filename):
    parser = PdfMinerParser()
    document = parser.parse_file(str(get_test_directory()) + filename + '.pdf')
    line_layout_analysis = LineLayoutAnalysis(document)
    return line_layout_analysis


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
    # filename = 'FRS189 Pricing Supplement 20190301'
    # filename = 'GRT30 Pricing Supplement 20181210.pdf-ocr'
    filename = 'CLN552 Pricing Supplement 20181214.pdf-ocr'
    text_layout_analysis = get_text_layout_analysis(filename)

    page_index_list = range(0,2)
    for page_index in page_index_list:
        page = text_layout_analysis.pages[page_index]
        print_page_details(page)


def test_distribution():
    filename = 'Distribution Sample'
    line_layout_analysis = get_line_layout_analysis(filename)

    for page in line_layout_analysis.pages:
        print_page_details(page)

#
# def test_semantic_ontology():
#     filename = 'OFSAA_DD_E16101_01'
#     line_layout_analysis = get_line_layout_analysis(filename)
#
#     for page in line_layout_analysis.pages[0:5]:
#         print_page_details(page)
