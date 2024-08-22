from pydantic import BaseModel, ConfigDict
from pylatex import Document, NoEscape, Package
from pylatex.base_classes import Options

from src.latex_styles.basic_settings import basic_package_settings, basic_settings
from src.latex_styles.doc_style import DocStyle
from src.latex_styles.emtpy_setting import empty_settings
from src.latex_styles.exam_settings import exam_settings


def set_preamble_no_escape(doc: Document, setting: str):
    doc.preamble.append(NoEscape(setting))


def set_preamble(doc: Document, setting: str):
    doc.preamble.append(setting)


def set_package_tuple(doc: Document, pkg_tuple: tuple[str, str]):
    package_name, option = pkg_tuple
    doc.preamble.append(Package(package_name, options=option))


def set_package(doc: Document, pkg: str):
    doc.preamble.append(Package(pkg))


def tex_file_up(doc: Document, filepath: str):
    doc.generate_tex(filepath=filepath)


class LatexStyle(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    doc: Document | None = None
    style: str | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doc = Document(
            documentclass='oblivoir',
            document_options=Options('10pt', 'oneside', 'chapter', 'adjustmath'),
            fontenc=None,
            inputenc=None,
            lmodern=False,
            textcomp=False,
            page_numbers=True,  # 이 옵션을 True로 설정
            geometry_options=None,
        )

    def __str__(self):
        package_list = []
        other_settings = []

        # 저장
        for item in self.doc.preamble:
            match item:
                case Package():  # 패키지인 경우
                    package_list.append(str(item))
                case _:  # 그 외의 경우
                    other_settings.append(str(item))

        # 포맷팅된 문자열 생성
        formatted_content = []

        if package_list:
            formatted_content.append("Packages:\n" + "\n".join(f"  - {pkg}" for pkg in package_list))

        if other_settings:
            formatted_content.append("Other Settings:\n" + "\n".join(f"  - {setting}" for setting in other_settings))

        return "\n\n".join(formatted_content)  # 패키지와 다른 설정을 두 줄 띄워서 구분

    def execute_style(self, style: DocStyle):
        match style:
            case DocStyle(type='package', settings=settings):
                self.set_packages(settings)

            case DocStyle(type='layout', settings=settings):
                self.set_layout(settings)

            case DocStyle(type='page', settings=settings):
                self.set_page_style(settings)

            case DocStyle(type='font', settings=settings):
                self.set_font_settings(settings)

            case DocStyle(type='command', settings=commands):
                self.set_custom_commands(commands)

            case _:
                raise ValueError("Unknown style type")

    def set_packages(self, package_list: list | None = None):
        for package in package_list:
            match package:
                case (package_name, option):
                    set_package_tuple(self.doc, (package_name, option))

                case str(package_name):
                    set_package(self.doc, package_name)

                case _:
                    raise ValueError(f"Unsupported package format: {package}")

        set_preamble_no_escape(self.doc, r'\tcbuselibrary{skins, breakable}')

    def set_layout(self, layout_settings: list[str]):
        for setting in layout_settings:
            set_preamble_no_escape(self.doc, setting=setting)

    def set_page_style(self, page_style_settings):
        for setting in page_style_settings:
            set_preamble_no_escape(self.doc, setting=setting)

    def set_font_settings(self, font_settings: list[str]):
        for setting in font_settings:
            set_preamble_no_escape(self.doc, setting=setting)

    def set_custom_commands(self, custom_commands: list[str] | None = None):
        if custom_commands is None:
            custom_commands = []
        for setting in custom_commands:
            set_preamble(self.doc, setting=setting)


def generate_tex_file(style_fac: LatexStyle):
    style_fac.execute_style(basic_package_settings)
    match style_fac:
        case LatexStyle(style='basic'):
            [style_fac.execute_style(setting) for setting in basic_settings]
        case LatexStyle(style='exam'):
            [style_fac.execute_style(setting) for setting in exam_settings]
        case LatexStyle(style='empty'):
            [style_fac.execute_style(setting) for setting in empty_settings]
        case _:
            raise ValueError("Unknown style type")

    def generate_tex(content, output_filename, post_compile):
        set_preamble_no_escape(style_fac.doc, content)
        tex_filename = f"{output_filename}.tex"
        tex_file_up(style_fac.doc, tex_filename)
        if post_compile:
            post_compile(content, tex_filename)

    return generate_tex


def add_head_comment(comment: str, filepath:str):
    with open(filepath, 'r+') as f:
        content = f.read()
        match comment in content:
            case True:  # comment 포함
                print("Comment already exists.")
            case False:  # comment가 포함되지 않음
                f.seek(0)
                f.write(comment + "\n" + content)


if __name__ == '__main__':
    # try exam setting
    latex_style = LatexStyle(style='exam')
    [latex_style.execute_style(setting) for setting in exam_settings]

    print(latex_style)
