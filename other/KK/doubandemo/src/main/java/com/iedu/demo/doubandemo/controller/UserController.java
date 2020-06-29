package com.iedu.demo.doubandemo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/logic/user")
@Controller
public class UserController {

    @RequestMapping("/login")
    public String login(String uid, String pwd, String nickName){
        System.out.println(uid + "," + pwd + "," + nickName);
        return "/index";
    }
}
