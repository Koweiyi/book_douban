package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.User;

import java.util.List;

public interface UserService {

    User login(String uid, String pwd);
    
    User addUser(User user);

    List<User> search(User user);
}
