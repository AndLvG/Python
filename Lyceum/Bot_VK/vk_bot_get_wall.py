import vk_api
import datetime


def main():
    login, password = '79109194537', 'a301301A!'
    # login, password = LOGIN, PASSWORD

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    response = vk.wall.get(count=5, offset=0)
    if response['items']:
        for i in response['items']:
            print(i['text'])
            dt = datetime.datetime.fromtimestamp(i['date'])
            print(f"date: {dt.strftime('%Y-%m-%d')}, time {dt.strftime('%H:%M:%S')}")

    # # Информация о друзьях
    # response = vk.friends.get(fields="bdate, city")
    # if response['items']:
    #     for i in response['items']:
    #         print(i)
    # response = vk.users.get(user_id=идентификатор_пользователя)
    # print(response)

    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_wall(['postman2.png'])

    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, vk_photo_id, sep="\n")
    vk = vk_session.get_api()
    vk.wall.post(message="Test", attachments=[vk_photo_id])


if __name__ == '__main__':
    main()
