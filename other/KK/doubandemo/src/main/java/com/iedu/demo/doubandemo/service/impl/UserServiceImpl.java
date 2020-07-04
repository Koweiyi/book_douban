package com.iedu.demo.doubandemo.service.impl;

import com.iedu.demo.doubandemo.dao.UserMapper;
import com.iedu.demo.doubandemo.entity.User;
import com.iedu.demo.doubandemo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserMapper mapper;

    @Override
    public User login(String uid, String pwd) {
        List<User> result= mapper.selectAll();
        for(int i = 0 ; i < result.size() ; i ++){
            if(result.get(i).getUid().equals(uid) && result.get(i).getPwd().equals(pwd))
                return new User (uid, pwd);
        }
        return null;
    }
}
