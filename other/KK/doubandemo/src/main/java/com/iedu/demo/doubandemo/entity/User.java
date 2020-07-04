package com.iedu.demo.doubandemo.entity;

import lombok.Data;

@Data
public class User {
    private int id;
    private String uid;
    private String pwd;
    private String nickName;

    public User(String uid, String pwd){
        this.uid = uid;
        this.pwd = pwd;
    }
}
