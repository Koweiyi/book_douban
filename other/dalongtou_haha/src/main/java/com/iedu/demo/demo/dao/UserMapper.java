package com.iedu.demo.demo.dao;

import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;
import com.iedu.demo.demo.entity.User;

import java.util.List;

@Repository
public interface UserMapper {

    @Select("select * from user limit 0, 30")
    public List<User> selectAll();

    @Select("select * from user where uid = #{uid} and pwd = #{pwd} and state = 1")
    public User login(@Param("uid") String uid, @Param("pwd") String pwd);

    @Select("select * from user where uid = #{uid}")
    public User seceltByUid(@Param("uid") String uid);

    @Insert("insert into user(uid,pwd,nick_name,state) values(#{user.uid},#{user.pwd},#{user.nickName},#{user.state})")
    @Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
    public int addUser(@Param("user") User user);

    @Update("update user set pwd = #{newPwd} where id = #{id}")
    int updatePwd(@Param("id") int id, @Param("newPwd") String newPwd);

}
