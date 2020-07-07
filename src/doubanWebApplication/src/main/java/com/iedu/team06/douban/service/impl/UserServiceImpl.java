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

        if(user != null && (user.getState() == 1 || user.getState() == 3))
            return user;
        return null;
    }

    @Override
    public boolean addUser(User user) {

        if(mapper.selectByUid(user.getUid()) == null){
            user.setState(1);
            mapper.addUser(user);
            return true;
        }

        return false;
    }

    @Override
    public List<User> search(User user) {
        return mapper.selectAll();
    }

    @Override
    public User searchOne(String uid) {
        return mapper.selectByUid(uid);
    }

    @Override
    public User edit(EditUserData editUserData) {

        int cnt = mapper.editByID(editUserData);
        if(cnt == 1)
            return new User(editUserData.getId(), editUserData.getNewNickName());
        return null;
    }

    @Override
    public boolean resetPwd(String id) {
        String defaultPwd = "000000";
        User oldUser = mapper.selectByUid(id);
        if(oldUser != null){
            oldUser.setPwd(defaultPwd);
            return mapper.update(oldUser) == 1;
        }
        return false;
    }

}
