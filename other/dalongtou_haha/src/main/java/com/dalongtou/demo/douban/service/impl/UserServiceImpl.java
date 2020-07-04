package com.dalongtou.demo.douban.service.impl;

import com.dalongtou.demo.douban.dao.UserMapper;
import com.dalongtou.demo.douban.entity.User;
import com.dalongtou.demo.douban.service.UserService;
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
        if(user != null && user.getstate() == 1)
            return user;
        return null ;
    }

    @Override
    public User addUser(User user) {

        if(mapper.selectByUid(user.getUid())==null){
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
}
