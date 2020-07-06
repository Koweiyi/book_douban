package com.iedu.team06.douban.service.impl;

import com.iedu.team06.douban.dao.UserMapper;
import com.iedu.team06.douban.entity.User;
import com.iedu.team06.douban.service.UserService;
import com.iedu.team06.douban.tools.EditUserData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserMapper mapper;

    @Override
    public User login(String uid, String pwd) {

        User user = mapper.login(uid, pwd);

        if(user != null && user.getState() == 1)
            return user;
        return null;
    }

    @Override
    public User addUser(User user) {

        if(mapper.selectByUid(user.getUid()) == null){
            user.setState(0);
            mapper.addUser(user);
            return user;
        }

        return null;
    }

    @Override
    public List<User> search(User user) {
        return mapper.selectAll();
    }

    @Override
    public User edit(EditUserData editUserData) {

        int cnt = mapper.editByID(editUserData);
        if(cnt == 1)
            return new User(editUserData.getId(), editUserData.getNewNickName());
        return null;
    }

}
