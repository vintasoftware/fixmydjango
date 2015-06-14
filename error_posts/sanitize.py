import re


def sanitize_traceback(tb):
    tb = tb.replace('\r', '')
    tb_sanitized_splitted = []
    file_re = re.compile(
        r'File \".+\",')
    deps_file_re = re.compile(
        r'File \".+((?:python.+)+?.+site-packages.+)\",')
    line_number_re = re.compile(
        r'line \d+, in .+')
    prev_line_was_pvt_file = False

    # remove empty lines
    all_tb_lines = [tb_line for tb_line in tb.split('\n')
                    if tb_line.strip()]

    for tb_line in all_tb_lines:
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
                        'File "?????.py",',
                        tb_line)
                    tb_line = line_number_re.sub(
                        'line ??, in ??????',
                        tb_line)
        else:  # prev_line_was_pvt_file
            prev_line_was_pvt_file = False
            tb_line = re.sub(
                r'(\s+).+',
                r'\1????????',
                tb_line)

        tb_sanitized_splitted.append(tb_line)

    if prev_line_was_pvt_file:
        raise ValueError(
            "Malformed traceback: ended with File line")

    return '\n'.join(tb_sanitized_splitted)
