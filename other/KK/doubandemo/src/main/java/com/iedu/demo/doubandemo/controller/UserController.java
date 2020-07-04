package com.iedu.demo.doubandemo.controller;

import com.iedu.demo.doubandemo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/logic/user")
@Controller
public class UserController {

    @Autowired
    private UserService service;

    @RequestMapping(value = "/login")
    public String login(String uid, String pwd, String nickName){

        if(service.login(uid, pwd) != null)
            return "redirect:/html/index.html";
        return "redirect:/html/login.html";
//        System.out.println(uid + "," + pwd + "," + nickName);
//        return "/index";
    }
}
