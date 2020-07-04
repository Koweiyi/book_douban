package com.dalongtou.demo.douban.entity;

import lombok.Data;

@Data
public class User {
    private  int id;
    private String uid;
    private String pwd;
    private String nickName;
    private int state;

    public User(String uid,String pwd,String nickName,int id,int state){
        this.uid = uid;
        this.pwd = pwd;
        this.id = id;
        this.nickName = nickName;
        this.state = state;
    }


    public int getstate() {

        return this.state;
    }
}
