package com.dalongtou.demo.douban.entity;

import lombok.Data;

@Data
public class User {
    private String uid;
    private String pwd;
    private String nickname;

    public User(String uid,String pwd){
        this.uid = uid;
        this.pwd = pwd;
    }

}
