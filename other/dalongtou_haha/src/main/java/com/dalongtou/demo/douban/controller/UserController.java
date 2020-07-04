package com.dalongtou.demo.douban.controller;

import com.dalongtou.demo.douban.entity.User;
import com.dalongtou.demo.douban.service.UserService;
import com.dalongtou.demo.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping(value = "/logic/user")
public class UserController {

    @Autowired
    private UserService service;

    @RequestMapping(value = "/login")
    public String login(String uid,String pwd,String nickname){

        System.out.println(uid+","+pwd+","+nickname);
        System.out.println("为啥没有呢？");
        if (service.login(uid,pwd) != null)
            return "redirect:/html/mainpage.html";

        return "redirect:/html/login.html";
    }

    @RequestMapping(value = "/add")
    @ResponseBody
    public User addUser(User user){

        User newUser = service.addUser(user);

        return  newUser;
    }

    @RequestMapping(value = "/search")
    @ResponseBody
    public TableData search(User user){

        TableData data = new TableData();
        List<User> result = service.search(user);
        data.setCode(0);
        data.setMsg("");
        data.setCount(result.size());
        data.setData(result);

        return data;
    }

}
