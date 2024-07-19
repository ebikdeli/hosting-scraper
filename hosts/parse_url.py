import os
import validators


def extract_host_file_urls(host_name:str) -> set:
    """Receive host_name -eg: 'parsvds'- as input and return urls founded in 'host_name.txt' as a set"""
    url_set = set()
    try:
        # Look for the urls in 'host.txt' file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(current_dir, host_name, f'{host_name}.txt')
        with open(file_name, 'rt') as f:
            url_list = f.readlines()
        # Parse and validate the extracted urls from the file
        for url in url_list:
            url = url.strip()
            if url.startswith('\n') or url.endswith('\n'):
                url = url.replace('\n', '')
            if not validators.url(url) or not f'{host_name}' in url:
                continue
            url_set.add(url)
    except FileNotFoundError as e:
        print(f'ERROR: NO FILE EXISTS AS "{host_name}.txt"\nCOMPLETE ERROR MESSAGE: {e.__str__()}')
    return url_set
