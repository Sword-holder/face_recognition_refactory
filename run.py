#!/usr/bin/env python
#coding=utf-8
# @Author: Xiao Ziyang
# @Description: 运行整个程序


from server import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)