import vk_api
import datetime


def main():
    login, password = '79109194537', 'a301301A!'
    # login, password = LOGIN, PASSWORD

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    # Информация о друзьях
    response = vk.friends.get(fields="bdate, city")
    if response['items']:
        fr = []
        for i in response['items']:
            fr.append([i['first_name'], i['last_name'], i['bdate']])
        fr = sorted(fr, key=lambda x: x[0])
        for i in fr:
            print(f'Друг {i[0]} {i[1]} др {i[2]}')


if __name__ == '__main__':
    main()
