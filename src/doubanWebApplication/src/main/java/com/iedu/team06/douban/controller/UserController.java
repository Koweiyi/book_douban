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
import org.springframework.web.bind.support.SessionStatus;

import javax.servlet.http.HttpSession;
import java.util.List;

@Controller
@RequestMapping("/logic/user")
@SessionAttributes("LoginUser")
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping(value = "/login")
    public String login(@RequestParam("uid") String uid, @RequestParam("pwd") String pwd, Model model){

        User user = userService.login(uid, pwd);
        if (user != null){
            model.addAttribute("LoginUser", user);
            return "redirect:/html/index.html";
        }
        return "redirect:/html/login.html";
    }

    @RequestMapping(value = "/LoginUser")
    @ResponseBody
    public User LoginUser(Model model){
        return  (User) model.getAttribute("LoginUser");
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
    public TableData search(User user,int page, int limit){

        TableData date = new TableData();
        List<User> result = userService.search(user, page, limit);
        date.setCode(0);
        date.setMsg("");
        date.setCount(userService.searchCount(user));
        date.setData(result);

        return date;
    }

    @RequestMapping(value = "/indexUser")
    @ResponseBody
    public Message indexUser(String uid){
        Message message = new Message();
        message.setContent("");
        message.setError(userService.searchOne(uid) != null);
        return message;
    }

    @RequestMapping(value = "/edit")
    @ResponseBody
    public User edit(EditUserData editUserData){
        User u = userService.edit(editUserData);
        return u;
    }

    @RequestMapping(value = "logout")
    public String logout(HttpSession session, SessionStatus sessionStatus){

        session.invalidate();
        sessionStatus.setComplete();
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

    @RequestMapping("/{id}")
    @ResponseBody
    public User info(@PathVariable("id") int id){
        User user = userService.getUserById(Integer.toString(id));
        return user;
    }

    @RequestMapping(value = "/setState")
    @ResponseBody
    public Message setState(String id, int state){
        Message message = new Message();
        message.setError(true);
        message.setContent("");

        if(userService.setState(id, state)){
            message.setError(false);
        }
        return message;
    }

}
