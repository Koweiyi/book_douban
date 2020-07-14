package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.User;
import com.iedu.team06.douban.tools.EditUserData;

import java.util.List;

public interface UserService {

    User login(String uid, String pwd);
    
    boolean addUser(User user);

    List<User> search(User user, int page, int limit);

    int searchCount(User user);

    User searchOne(String uid);

    User edit(EditUserData editUserData);

    boolean resetPwd(String id);

    User getUserById(String id);

    boolean setState(String id, int state);

    boolean userTest(String uid, String pwd);

    boolean updateUser(String uid, String nickName, String pwd);
}
