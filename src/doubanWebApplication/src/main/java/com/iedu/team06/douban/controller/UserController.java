package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.User;
import com.iedu.team06.douban.service.UserService;
import com.iedu.team06.douban.tools.EditUserData;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpSession;
import java.util.List;

@Controller
@RequestMapping("/logic/user")
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping(value = "/login")
    public String login(@RequestParam("uid") String uid, @RequestParam("pwd") String pwd, HttpSession session){

        User user = userService.login(uid, pwd);
        if (user != null){
            session.setAttribute("LoginUser", user);
            return "redirect:/html/index.html";
        }
        return "redirect:/html/login.html";
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

    @RequestMapping(value = "/edit")
    @ResponseBody
    public User edit(EditUserData editUserData){

        User u = userService.edit(editUserData);
        return u;
    }

}
