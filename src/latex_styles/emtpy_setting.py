from src.latex_styles.doc_style import DocStyle

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
page_style_settings = [
    r'\makepagestyle{EmptyPage}',
    r'\makerunningwidth{EmptyPage}{\textwidth}',
    r'\makeatletter',
    r'\makeoddhead{EmptyPage}{}{}{}',
    r'\makeevenhead{EmptyPage}{}{}{}',
    r'\makeoddfoot{EmptyPage}{}{}{}',
    r'\makeevenfoot{EmptyPage}{}{}{}',
    r'\pagestyle{EmptyPage}'
]
font_settings = [
    r'\setkosansfont(NanumMyeongjo)(NanumMyeongjo Bold)()',
    r'\setkomainfont(NanumGothic)(NanumGothic Bold)()',
    r'\setmathhangulfont{NanumMyeongjo}'
]

empty_layout_settings = DocStyle(type='layout', settings=layout_settings)
empty_page_style_settings = DocStyle(type='page', settings=page_style_settings)
empty_font_settings=DocStyle(type='font', settings=font_settings)

empty_settings = [empty_layout_settings, empty_font_settings, empty_page_style_settings]