from pylatex import Document, Package, NoEscape
from pylatex.base_classes import Options
from abc import ABC, abstractmethod




class EmptyStyle(BaseLatexStyle):
    def get_layout_settings(self):
        return [
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

    def get_page_style_settings(self):
        return [
            r'\makepagestyle{EmptyPage}',
            r'\makerunningwidth{EmptyPage}{\textwidth}',
            r'\makeatletter',
            r'\makeoddhead{EmptyPage}{}{}{}',
            r'\makeevenhead{EmptyPage}{}{}{}',
            r'\makeoddfoot{EmptyPage}{}{}{}',
            r'\makeevenfoot{EmptyPage}{}{}{}',
            r'\pagestyle{EmptyPage}'
        ]

    def get_font_settings(self):
        # 기본 폰트 설정
        return [
            r'\setkosansfont(NanumMyeongjo)(NanumMyeongjo Bold)()',
            r'\setkomainfont(NanumGothic)(NanumGothic Bold)()',
            r'\setmathhangulfont{NanumMyeongjo}'
        ]

    def generate_tex_file(self, content, output_filename):
        self.doc.append(NoEscape(content))
        tex_filename = f"{output_filename}.tex"
        self.doc.generate_tex(output_filename)


class ExaminationStyle(BaseLatexStyle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.doc.preamble.append(NoEscape(r'\twocolumn'))

    def get_layout_settings(self):
        return [
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

    def get_page_style_settings(self):
        return [
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

    def get_font_settings(self):
        # 기본 폰트 설정
        return [
            r'\setkormainfont(HCRBatangLVT-Bold)(HCRBatangLVT-Bold){HCRBatangLVT}(HCRBatangLVT-Bold)(HCRBatangLVT){HCRBatangLVT}',
            r'\setkorsansfont(HCRDotumLVT-Bold)(HCRDotumLVT-Bold){HCRDotumLVT}(HCRDotumLVT-Bold)(HCRDotumLVT){HCRDotumLVT}',
            r'\setmathhangulfont{HCRBatangLVT}'
            r'\def\Exercisenumberfont{\fontspec[Ligatures=TeX]{Dinlig}}'
            r'\def\Solutionnumberfont{\fontspec[Ligatures=TeX]{Dinlig}}'
        ]

    def get_custom_commands(self):
        return [
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

    def generate_tex_file(self, content, output_filename):
        self.doc.append(NoEscape(content))
        tex_filename = f"{output_filename}.tex"
        self.doc.generate_tex(output_filename)

        # 매직 코멘트 추가
        with open(tex_filename, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write("% !TEX TS-program = xelatex\n" + content)

        return tex_filename

# 스타일 팩토리
class StyleFactory:
    @staticmethod
    def get_style(style_name):
        if style_name == "Empty":
            return EmptyStyle()
        elif style_name == "Examination":
            return ExaminationStyle()
        else:
            raise ValueError(f"Unknown style: {style_name}")