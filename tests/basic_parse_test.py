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


def test_mifid_regulation_parse_to_lines():
    filename = 'MIFID_20140917'
    text_layout_analysis = get_text_layout_analysis(filename)
    page_index_list = [25, 29, 31, 37, 131]
    for page_index in page_index_list:
        page = text_layout_analysis.pages[page_index]
        print_page_details(page)

    page = text_layout_analysis.pages[25]
    assert(len(page.content_areas) == 18)

    # Page 30 (Article 2, 4)
    page = text_layout_analysis.pages[29]
    assert(len(page.content_areas) == 19)

    # Page 32 (Article 4)
    page = text_layout_analysis.pages[31]
    assert(len(page.content_areas) == 16)
    assert(page.content_areas[7].as_string().startswith('Article'))

    # Page 38 (Article 4 1, 1, 55)
    page = text_layout_analysis.pages[37]
    assert(len(page.content_areas) == 18)
    assert(page.content_areas[10].as_string().startswith('(55)'))

    # Page 132 is the last page for Regs
    page = text_layout_analysis.pages[131]
    assert(15 <= len(page.content_areas) <= 17)
    assert(page.content_areas[4].as_string().startswith('Article'))


def test_mifir_regulation_parse_to_lines():
    filename = 'MIFIR_20140612'
    text_layout_analysis = get_text_layout_analysis(filename)

    page_index_list = [11]
    for page_index in page_index_list:
        page = text_layout_analysis.pages[page_index]
        print_page_details(page)

    # Page 12 (TITLE I, Article 1)
    page = text_layout_analysis.pages[11]
    assert(len(page.content_areas) == 15)
    assert(len(page.content_areas[9].lines) == 1)
    assert(len(page.content_areas[14].lines) == 1)


def test_emir_regulation_parse_to_lines():
    filename = 'EMIR_20120727'
    text_layout_analysis = get_text_layout_analysis(filename)
    page_index_list = [55, 56]
    for page_index in page_index_list:
        page = text_layout_analysis.pages[page_index]
        print_page_details(page)

    # Page 56 has the last node
    page = text_layout_analysis.pages[55]
    assert(19 <= len(page.content_areas) <= 21)
    assert(page.content_areas[7].as_string().startswith('Article'))


def test_mifir_rts22_regulation_parse_to_lines():
    filename = 'MIFIR_RTS_22'
    text_layout_analysis = get_text_layout_analysis(filename)

    page_index_list = range(0,8)
    for page_index in page_index_list:
        page = text_layout_analysis.pages[page_index]
        print_page_details(page)

    # Page 7 (Article 1)
    page = text_layout_analysis.pages[6]
    assert(len(page.content_areas) == 12)
    assert(len(page.content_areas[6].lines) == 2)
    assert(len(page.content_areas[7].lines) == 5)
    assert(len(page.content_areas[8].lines) == 2)


def test_mifir_qas():
    filename =  'MIFIR_QAs_20190409'
    text_layout_analysis = get_text_layout_analysis(filename)

    page_index_list = range(0, 8)
    for page_index in page_index_list:
        page = text_layout_analysis.pages[page_index]
        print_page_details(page)

    # First page has two images
    page = text_layout_analysis.pages[0]
    assert(page.content_areas[0].features.image_node)
    assert(page.content_areas[4].features.image_node)


def test_table_code():
    filename =  'MIFIR_QAs_table_sample_p21'
    text_layout_analysis = get_text_layout_analysis(filename)

    page = text_layout_analysis.pages[0]
    assert(page.content_areas[0].features.image_node)


def test_china_reg():
    filename = 'CHN76384Eng_20070629'
    text_layout_analysis = get_text_layout_analysis(filename)

    lines_to_print = text_layout_analysis.pages[2].content_areas[2].lines
    for line in lines_to_print:
        print(line.as_string())
    page = text_layout_analysis.pages[0]

