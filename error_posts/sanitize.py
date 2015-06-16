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


def sanitize_traceback(clean_tb):
    tb_sanitized_splitted = []
    file_re = re.compile(
        r'File \".+\",')
    deps_file_re = re.compile(
        r'File \".+((?:python.+)+?.+site-packages.+)\",')
    line_number_re = re.compile(
        r'line \d+, in .+')
    prev_line_was_pvt_file = False

    for tb_line in clean_tb.split('\n'):
        if not prev_line_was_pvt_file:
            file_re_match = file_re.search(tb_line)

            if file_re_match:
                deps_file_re_match = deps_file_re.search(tb_line)

                if deps_file_re_match:
                    prev_line_was_pvt_file = False
                    tb_line = deps_file_re.sub(
                        r'File "\1",',
                        tb_line)
                else:
                    prev_line_was_pvt_file = True
                    tb_line = file_re.sub(
                        'File "private.py",',
                        tb_line)
                    tb_line = line_number_re.sub(
                        'line 1, in private_function',
                        tb_line)
        else:  # prev_line_was_pvt_file
            prev_line_was_pvt_file = False
            tb_line = re.sub(
                r'(\s+).+',
                r'\1private_function()',
                tb_line)

        tb_sanitized_splitted.append(tb_line)

    return '\n'.join(tb_sanitized_splitted)
