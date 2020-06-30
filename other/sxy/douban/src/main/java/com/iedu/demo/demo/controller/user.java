package com.iedu.demo.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import com.iedu.demo.demo.service.UserService;
@RequestMapping("/logic/user")
@Controller
public class user {
    @Autowired
    private  UserService service
    @RequestMapping(value = "/login")
    public String login(String uid,String pwd,String nickName) {
        if(service.login(uid,pwd) != null)
            return "redirect:/html/mainpage.html"

        return "redirect:/html/login.html";
    }
}
