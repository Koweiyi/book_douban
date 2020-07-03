package com.iedu.demo.demo.service;

import com.iedu.demo.demo.entity.User;

import java.util.List;

public interface UserService {

    User login(String uid, String pwd);

    User addUser(User user);

    List<User> search(User user);

    boolean resetPwd(int id);
}
