import re


_exception_re = re.compile(r'\w+: .*')


def clean_traceback(tb):
    # remove \r
    tb = tb.replace('\r', '')

    # remove empty lines
    all_tb_lines = [tb_line for tb_line in tb.split('\n')
                    if tb_line.strip()]

    # check conditions
    last_deps_line = all_tb_lines[-3]
    django_index = last_deps_line.find('/django')
    if django_index == -1:
        raise ValueError(
            "Invalid traceback: exception not thrown by Django")

    last_line = all_tb_lines[-1] = all_tb_lines[-1].lstrip()
    exception_re_match = _exception_re.match(last_line)
    if not exception_re_match:
        raise ValueError(
            "Malformed traceback: last line must be "
            "exception type and message")

    return '\n'.join(all_tb_lines)


def sanitize_traceback(tb):
    # TODO
    return tb
