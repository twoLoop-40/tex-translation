from pylatex import NoEscape

from src.latex_styles.doc_style import DocStyle

layout_settings = [
    r'\setstocksize{326.7mm}{231mm}',
    r'\settrimmedsize{\stockheight}{\stockwidth}{*}',
    r'\settypeblocksize{287.7mm}{215mm}{*}',
    r'\setlrmargins{8mm}{*}{*}',
    r'\setulmargins{17mm}{*}{*}',
    r'\setheadfoot{\onelineskip}{2\onelineskip}',
    r'\setheaderspaces{*}{\onelineskip}{*}',
    r'\setcolsepandrule{5mm}{0.5pt}',
    r'\checkandfixthelayout',
    r'\pdfpagewidth\paperwidth',
    r'\pdfpageheight\paperheight',
    r'\setlength\parindent{0pt}'
]

page_style_settings = [
    r'\makepagestyle{Examination}',
    r'\makerunningwidth{Examination}{\textwidth}',
    r'\makeatletter',
    r'\makeoddhead{Examination}{}{}{}',
    r'\makeevenhead{Examination}{}{}{}',
    r'\makeoddfoot{Examination}{}{}{}',
    r'\makeevenfoot{Examination}{}{}{}',
    r'\pagestyle{Examination}',
    r'\makechapterstyle{Examination}{%',
    r'\setlength{\beforechapskip}{2\onelineskip}',
    r'\setlength{\afterchapskip}{8\onelineskip}',
    r'\setlength{\midchapskip}{2\onelineskip}',
    r'\renewcommand{\chaptitlefont}{\sffamily}',
    r'\renewcommand{\prechapternum}{}',
    r'\renewcommand{\postchapternum}{}',
    r'\renewcommand{\chapternamenum}{}',
    r'\renewcommand{\printchapternum}{}',
    r'\renewcommand{\printchaptertitle}[1]{%',
    r'\thispagestyle{empty}',
    r'\begin{flushright}',
    r'{\chaptitlefont ##1}',
    r'\end{flushright}',
    r'}}',
    r'\makeatother',
    r'\AtBeginDocument{\oblivoirchapterstyle{Examination}}',
]

font_settings = [
    r'\setkormainfont(HCRBatangLVT-Bold)(HCRBatangLVT-Bold){HCRBatangLVT}(HCRBatangLVT-Bold)(HCRBatangLVT){HCRBatangLVT}',
    r'\setkorsansfont(HCRDotumLVT-Bold)(HCRDotumLVT-Bold){HCRDotumLVT}(HCRDotumLVT-Bold)(HCRDotumLVT){HCRDotumLVT}',
    r'\setmathhangulfont{HCRBatangLVT}'
    r'\def\Exercisenumberfont{\fontspec[Ligatures=TeX]{Dinlig}}'
    r'\def\Solutionnumberfont{\fontspec[Ligatures=TeX]{Dinlig}}'
]

custom_commands = [
    NoEscape(r'\newcounter{ExerciseCTR}\newsavebox{\ExerciseCTR}'),
    NoEscape(r'\renewcommand{\theExerciseCTR}{\arabic{ExerciseCTR}}'),
    NoEscape(
        r'\newcommand{\TypeExerciseCTR}{\stepcounter{ExerciseCTR}{\huge\Exercisenumberfont\theExerciseCTR}}'),
    NoEscape(r'\newcounter{SolutionCTR}\newsavebox{\SolutionCTR}'),
    NoEscape(r'\renewcommand{\theSolutionCTR}{\arabic{SolutionCTR}}'),
    NoEscape(
        r'\newcommand{\TypeSolutionCTR}{\stepcounter{SolutionCTR}{\huge\theSolutionCTR}}'),
    NoEscape(r'\newcommand{\resetCTR}{\setcounter{ExerciseCTR}{0}\setcounter{SolutionCTR}{0}}'),
]

exam_layout_settings = DocStyle(type='layout', settings=layout_settings)
exam_page_style_settings = DocStyle(type='page', settings=page_style_settings)
exam_font_settings = DocStyle(type='font', settings=font_settings)
exam_custom_commands = DocStyle(type='command', settings=custom_commands)

exam_settings = [exam_layout_settings, exam_page_style_settings, exam_font_settings, exam_custom_commands]