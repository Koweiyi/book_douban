package com.dalongtou.demo.douban.service;

import com.dalongtou.demo.douban.entity.User;

public interface UserService {
    User login(String uid, String pwd);
}
