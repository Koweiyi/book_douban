package com.iedu.demo.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/logic/user")
@Controller
public class user {
    public String login(String uid,String pwd,String nickName) {
        System.out.println(uid + ", " + pwd + ", " + nickName);
        return "mainpage";
    }
}
