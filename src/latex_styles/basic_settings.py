from src.latex_styles.doc_style import DocStyle

package_settings = [
    'xcolor',
    'mathtools',
    'graphicx',
    'tabularray',
    ('koredumath', 'eqnformat=circdots, similarsignfig, mathbb'),
    ('nvverttab', 'numvtabs=2'),
    'tcolorbox',
    'pgf',
    'tikz',
    'pgfplots'
]
layout_settings = [
    r'\setstocksize{326.7mm}{110mm}',
    r'\settrimmedsize{\stockheight}{\stockwidth}{*}',
    r'\settypeblocksize{287.7mm}{105mm}{*}',
    r'\setlrmargins{2mm}{*}{2mm}',
    r'\setulmargins{17mm}{*}{*}',
    r'\setheadfoot{\onelineskip}{2\onelineskip}',
    r'\setheaderspaces{*}{\onelineskip}{*}',
    r'\setmarginnotes{1mm}{1mm}{\onelineskip}',
    r'\checkandfixthelayout',
    r'\pdfpagewidth\paperwidth',
    r'\pdfpageheight\paperheight',
    r'\setlength\parindent{0pt}'
]
font_settings = [
    r'\setkosansfont(NanumMyeongjo)(NanumMyeongjo Bold)()',
    r'\setkomainfont(NanumGothic)(NanumGothic Bold)()',
    r'\setmathhangulfont{NanumMyeongjo}'
]
page_style_settings = [
    r'\pagestyle{plain}'  # 또는 원하는 다른 기본 페이지 스타일
]

basic_package_settings = DocStyle(type='package', settings=package_settings)
basic_layout_settings = DocStyle(type='layout', settings=layout_settings)
basic_font_settings = DocStyle(type='font', settings=font_settings)
basic_page_style_settings = DocStyle(type='page', settings=page_style_settings)

basic_settings = [basic_layout_settings, basic_font_settings, basic_page_style_settings]