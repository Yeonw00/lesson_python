# 이 파일이 무슨 역할을 하는지 설명
"""Utils to display to be returned to the user on the console."""
import os
import string

import termcolor


def get_template_dir_path():
    # 함수의 활용방법 서술
    """Return the path of the template's directory.

    Returns:
        str: The template dir path.
    """
    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path

    Raises:
        NoTemplateError: If the file does not exists.
    """
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))
    return temp_file_path


def get_template(template_file_path, color=None):
    """Return the path of the template.

    # 인수에 대한 설명
    Args:
        template_file_path (str): The template file path
        color: (str): Color formatting for output in terminal
            See in more details: https://pypi.python.org/pypi/termcolor

    # 반환값에 대해서 설명
    Returns:
        string.Template: Return templates with characters in templates.
    """
    template = find_template(template_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)


"""
pylint ranking.py 실행 시 출력 값 

************* Module src.lesson_250416.roboter.models.ranking
# TODO가 있다는 의미
ranking.py:66:9: W0511: TODO (jsakai) Use locking mechanism for avoiding dead lock issue (fixme)
ranking.py:16:0: R0205: Class 'CsvModel' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
# 별로 안쓰는데 정의된 메소드가 있다는 의미
ranking.py:16:0: R0903: Too few public methods (0/2) (too-few-public-methods)
ranking.py:26:4: W1113: Keyword argument before variable positional arguments list in the definition of __init__ function (keyword-arg-before-vararg)
ranking.py:41:12: C0415: Import outside toplevel (settings) (import-outside-toplevel)
ranking.py:57:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
ranking.py:67:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

-----------------------------------
Your code has been rated at 8.75/10

# 메소드에 대한 document가 없을때는 아래와 같은 메시지가 뜸
Missing method docstring (missing-docstring)

"""