package com.dalongtou.demo.douban.controller;

import com.dalongtou.demo.douban.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

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
}
