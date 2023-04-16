import os
import time
import requests
import urllib
import magic
import progressbar
from urllib.parse import quote


def __init__():
    pass


def _create_directories(_directory, _name):
    """
    create directory to save images
    :param _directory:
    :param _name:
    :return:
    """
    name = _name.replace(" ", "_")
    try:
        if not os.path.exists(_directory):
            os.makedirs(_directory)
            time.sleep(0.2)
            path = name
            sub_directory = os.path.join(_directory, path)
            if not os.path.exists(sub_directory):
                os.makedirs(sub_directory)
        else:
            path = name
            sub_directory = os.path.join(_directory, path)
            if not os.path.exists(sub_directory):
                os.makedirs(sub_directory)

    except OSError as e:
        if e.errno != 17:
            raise
        pass
    return


def _download_page(url):

    try:
        headers={}
        headers[
            'User-Agent']="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())
        return respData

    except Exception as e:
        print(e)
        exit(0)


def download(keywords, limit, directory='', extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'}):
    """
    download images from google images
    :param keywords:
    :param limit:
    :param directory:
    :param extensions:
    :return:
    """
    keyword_to_search = [str(item).strip() for item in keywords.split(',')]
    if directory != '':
        main_directory = directory
    else:
        main_directory = "images/"

    i = 0

    things = len(keyword_to_search) * limit

    bar = progressbar.ProgressBar(maxval=things, \
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    bar.start()

    while i < len(keyword_to_search):
        _create_directories(main_directory, keyword_to_search[i])
        url = 'https://www.google.com/search?q=' + quote(
            keyword_to_search[i].encode(
                'utf-8')) + '&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'
        raw_html = _download_page(url)

        end_object = -1;
        google_image_seen = False;
        j = 0
        while j < limit:
            while (True):
                try:
                    new_line = raw_html.find('"https://', end_object + 1)
                    end_object = raw_html.find('"', new_line + 1)

                    buffor = raw_html.find('\\', new_line + 1, end_object)
                    if buffor != -1:
                        object_raw = (raw_html[new_line + 1:buffor])
                    else:
                        object_raw = (raw_html[new_line + 1:end_object])

                    if any(extension in object_raw for extension in extensions):
                        break

                except Exception as e:
                    break
            path = main_directory + keyword_to_search[i].replace(" ", "_")

            try:
                r = requests.get(object_raw, allow_redirects=True, timeout=1)
                if ('html' not in str(r.content)):
                    mime = magic.Magic(mime=True)
                    file_type = mime.from_buffer(r.content)
                    file_extension = f'.{file_type.split("/")[1]}'
                    if file_extension not in extensions:
                        raise ValueError()
                    if file_extension == '.png' and not google_image_seen:
                        google_image_seen = True
                        raise ValueError()
                    if j+1 > 2: # solves the issue of first two images (ignore them)
                    # not sure why that happens, but a temporary solution while saving the images.
                        file_name = str(keyword_to_search[i]) + "_" + str(j + 1) + file_extension
                        with open(os.path.join(path, file_name), 'wb') as file:
                            file.write(r.content)
                    bar.update(bar.currval + 1)
                else:
                    j -= 1
            except Exception as e:
                j -= 1
            j += 1

        i += 1
    bar.finish()
