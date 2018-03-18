def download(url, out_path=None, get_headers=False, get_body=None):#TODO: Set cookies, user agent, headers manually, TODO: Handle Google Drive links, etc.
    from urllib.request import urlopen
    try:
        if all([protocol not in url[:8] for protocol in ('http://', 'https://')]):
            try_url = 'http://' + url
            result = urlopen(try_url)

            if result.getcode() != 200:
                try_url = 'https://' + url
                result = urlopen(try_url)
        else:
            result = urlopen(url)

        _headers, _body = bytes(result.headers), result.read()
    except:
        raise ConnectionError(-1, 'Could not access url', url)

    ret = bytes()
    if get_headers:#TODO: If only headers requested, then do a HEAD request instead of a GET
        ret += _headers
    else:
        if get_body is None:
            get_body = True

    if get_body:
        ret += _body

    if out_path is not None:
        with open(out_path, 'wb') as file:
            file.write(ret)

    if len(ret) == 0:
        ret = None

    return ret