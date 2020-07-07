package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.User;
import com.iedu.team06.douban.service.UserService;
import com.iedu.team06.douban.tools.EditUserData;
import com.iedu.team06.douban.tools.Message;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpSession;
import java.util.List;

@Controller
@RequestMapping("/logic/user")
@SessionAttributes("LoginUser")
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
    public String addUser(User user, String rePwd){

        if(user.getPwd().equals(rePwd)){
            if(userService.addUser(user))
                return "redirect:/html/login.html";
        }
        return "redirect/html/register.html";
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

    @RequestMapping(value = "logout")
    public String logout(Model model, HttpSession session){

        return "redirect:/html/login.html";

    }

    @RequestMapping(value = "/resetPwd")
    @ResponseBody
    public Message resetPwd(String id){
        Message message = new Message();
        message.setError(true);
        message.setContent("服务器错误，请重新尝试！");

        if(userService.resetPwd(id)){
            message.setError(false);
            message.setContent("密码重置已完成！");
        }
        return message;
    }
}
