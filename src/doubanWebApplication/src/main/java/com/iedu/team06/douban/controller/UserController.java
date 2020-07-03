package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.User;
import com.iedu.team06.douban.service.UserService;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping("/logic/user")
public class UserController {

    @Autowired
    private UserService userService;

    @RequestMapping(value = "/login")
    public String login(String uid, String pwd, String nickName){

        if (userService.login(uid, pwd) != null)
            return "redirect:/html/index.html";
        return "redirect/html/login.html";
    }

    @RequestMapping(value = "/add")
    @ResponseBody
    public User addUser(User user){
        return userService.addUser(user);
    }

    @RequestMapping(value = "/search")
    @ResponseBody
    public TableData search(User user){

        TableData tableData = new TableData();
        List<User> list = userService.search(user);
        tableData.setCode(0);
        tableData.setMsg("");
        tableData.setCount(list.size());
        tableData.setData(list);

        return tableData;
    }
}
