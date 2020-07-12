
#def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'.encode('unicode-escape').decode()):
def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime('%Y{0} %m{1} %d{2}').format(*'년월일')
    #https://hcid-courses.github.io/TA/QnA/issues_with_windows_korean_strftime.html