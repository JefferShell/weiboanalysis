
def format_date(date_string):
    from datetime import datetime
    return datetime.strptime(date_string, '%Y-%m-%d').strftime('%Y年%m月%d日')

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    return True
