import vk_api
import datetime
import os

TOKEN = 'aeea642e6d43e6a3ff5e068a1e455a7746f928aec2a3a771c4566a841eac45e620fed710abe7a14971ac6'


def main():
    login, password = '79109194537', 'a301301A!'
    # login, password = LOGIN, PASSWORD

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)
    root_dir = os.path.abspath(os.path.dirname(__file__))
    dir = os.path.join(root_dir, 'static', 'img')
    images = list(map(lambda x: os.path.join(dir, x), os.listdir(dir)))
    print(*images)

    upload.photo(images, album_id=274660470, group_id=195095163)


if __name__ == '__main__':
    main()
