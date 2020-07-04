package com.dalongtou.demo.douban.dao;

import com.dalongtou.demo.douban.entity.User;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserMapper {

    @Select("select * from user")
    public List<User> selectAll();

    @Select("select *from user where uid = #{uid} and pwd = #{pwd}")
    public User login(@Param("uid") String uid,@Param("pwd") String pwd);

    @Select("select *from user where uid = #{uid}")
    public User selectByUid(@Param("uid") String uid);

    @Insert("insert into user(uid,pwd,nickname)"+
            "values(#{user.uid},#{user.pwd},#{user.nickname},#{user.state})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    public int addUser(@Param("user") User user);

    @Update("update user set pwd = #{newPwd} where id = #{id}" )
    int updatePwd(@Param("id") int id, @Param( "newPwd") String newPwd) ;

}
