package com.iedu.demo.demo.service.impl;

import com.iedu.demo.demo.entity.User;
import com.iedu.demo.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.iedu.demo.demo.dao.UserMapper;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserMapper mapper;

    @Override
    public User login(String uid, String pwd){

        User user = mapper.login(uid,pwd);
        if (user != null && user.getState() == 1)
            return user;
        return null;

    }
    @Override
    public User addUser(User user){
        if (mapper.seceltByUid(user.getUid())==null){
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
    public boolean resetPwd(int id){
        String defaultPwd = "000000";

        if(mapper.updatePwd(id,defaultPwd)==1)
            return true;
        return false;
    }
}
