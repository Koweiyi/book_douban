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
    public List<User> search(User user, int page, int limit) {
        if (user != null && !"".equals(user.getUid().trim())) {
            user.setUid("%" + user.getUid() + "%");
        }
        if (page > 0 && limit > 0)
            return mapper.selectByWhere(user, (page-1) * limit, limit);
        return mapper.selectByWhere(user, null, null);
    }

    @Override
    public int searchCount(User user) {

        return mapper.countSelectByWhere(user);
    }


    @Override
    public boolean resetPwd(int id){
        String defaultPwd = "000000";

        if(mapper.updatePwd(id,defaultPwd)==1)
            return true;
        return false;
    }
}
