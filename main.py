import requests

url_img = 'url'
url_video = 'url'


def download_img(url=''):

    try:
        response = requests.get(url=url)

        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)
            return 'Img it is good '

    except Exception as ex:
        return 'Have error' + str(ex)


def download_video(url=''):

    try:
        response = requests.get(url=url)

        with open('req_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024*1024):
                if chunk:
                    file.write(chunk)

    except Exception as ex:
        return 'Have error' + str(ex)


def main():
    print(download_img(url=url_img))
    print(download_video(url=url_video))


if __name__ == '__main__':
    main()
