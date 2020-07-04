package com.dalongtou.demo.douban.service;

import com.dalongtou.demo.douban.dao.UserMapper;
import com.dalongtou.demo.douban.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
public interface UserService {
    User login(String uid, String pwd);

    User addUser(User user);

    List<User> search(User user);

    boolean resetPwd(int id);
}
