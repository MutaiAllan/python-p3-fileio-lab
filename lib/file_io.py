def write_file(file_name='/home/mutai/Development/code/phase3/week3/python-p3-fileio-lab/lib/test_file.txt', file_content='Added this text'):
    with open(file_name, mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)

def append_file(file_name='/home/mutai/Development/code/phase3/week3/python-p3-fileio-lab/lib/test_file.txt', append_content='Added this text'):
    with open(file_name, mode='a', encoding='utf-8') as log_file:
        log_file.write(append_content)

def read_file(file_name='/home/mutai/Development/code/phase3/week3/python-p3-fileio-lab/lib/test_file.txt'):
    with open(file_name, mode='r', encoding='utf-8') as log_file:
        log_file.read()