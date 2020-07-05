package com.iedu.demo.demo.controller;

import com.iedu.demo.demo.entity.User;
import com.iedu.demo.demo.tools.Message;
import com.iedu.demo.demo.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import com.iedu.demo.demo.service.UserService;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping("/logic/user")
public class Usercontroller {
    @Autowired
    private  UserService service;

    @RequestMapping(value = "/login", method = {RequestMethod.POST, RequestMethod.GET})
    public String login(String uid,String pwd,String nickName) {

        if(service.login(uid, pwd) != null)
            return "redirect:/html/mainpage.html";

        return "redirect:/html/login.html";
    }

    @RequestMapping(value = "/add")
    @ResponseBody
    public User addUser(User user){

        User newUser = service.addUser(user);

        return newUser;
    }

    @RequestMapping(value="/search")
    @ResponseBody
    public TableData search(User user, int page, int limit) {

        TableData date = new TableData();
        List<User> result = service.search(user, page, limit);
        date.setCode(0);
        date.setMsg("");
        date.setCount(service.searchCount(user));
        date.setData(result);

        return date;
    }

    @RequestMapping(value="/pwdreset")
    @ResponseBody
    public Message pwdReset(int id){
        Message msg = new Message();

        msg.setError(true);
        msg.setContent("服务器错误");

        if(service.resetPwd(id)){
            msg.setError(false);
            msg.setContent("密码已经更新");
        }
        return msg;
    }
}
