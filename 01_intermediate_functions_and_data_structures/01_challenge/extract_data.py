import re

def extract_data(text):
    pattern = r'\b[0-9a-zA-Z]+:[0-9a-zA-Z]+\b'
    matches = re.findall(pattern, text)

    return matches

def better_extract_data(text):
    pattern = r'\b([0-9a-zA-Z]+):([0-9a-zA-Z]+)\b'
    matches = re.findall(pattern, text)

    return matches
