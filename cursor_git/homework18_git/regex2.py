import re

with open("django_success (2).log.txt") as log_file:
    logfile = ''.join(log_file.read())
    result = re.sub(r'\[\d+\/\w+\/\d+\s\d+:\d+:\d+\]', "xx/xx/xx xx:xx:xx", logfile)
    result = re.sub(r'\/admin\S*', "/secret/address", result)
    with open('results.txt', 'w') as result_file:
        result_file.write(result)
    exit(0)
exit(0)
