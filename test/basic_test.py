from API import add_face, check_person, parse_result
import os
import json

def batch_login(file_folder):
    file_folder_path = os.getcwd() + '/' + file_folder
    image_name_list = os.listdir(file_folder_path)
    uid_list = [os.path.splitext(fullname)[0] for fullname in image_name_list]
    for i in range(len(uid_list)):
        res = add_face(uid_list[i], 'name', file_folder + image_name_list[i])
        code = parse_result(res, 'code')
        assert (code == 0) # 断言添加成功
        print('成功添加用户' + uid_list[i])
    print('已成功添加' + str(len(uid_list)) + '个用户！')
    return uid_list


def rotational_test(logined_uid_list, file_folder):
    file_folder_path = os.getcwd() + '/' + file_folder
    image_name_list = os.listdir(file_folder_path)
    for image in image_name_list: # 文件夹下所有图片
        for logined_uid in logined_uid_list:
            print('path==' + file_folder + image)
            res = check_person(logined_uid, 'name', file_folder + image)
            code = parse_result(res, 'code')
            assert (code == 0) # 断言认证成功
            print('提交成功，开始验证。。。。')
            simResult = parse_result(res, 'simResult', inside_data=True)
            print('upload:uid=' + str(logined_uid))
            if (image.split('_')[0] == logined_uid):
                assert (simResult == '1')
            else:
                assert (simResult == '0')
            print('通过测试用例' + image)

    print('循环测试通过！')

if __name__ == '__main__':
    logined_uid_list = batch_login('login_face/batch_01/') #批量添加人脸
    rotational_test(logined_uid_list, 'check_face/') #进行循环测试
    #for i in range(20):
    #    check_person('trump', 'check_face/trump_2.jpg')
