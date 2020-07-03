package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.User;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Options;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserMapper {

    @Select("select * from user limit 0, 30")
    public List<User> selectAll();

    @Select("select * from user where uid = #{uid} and pwd = #{pwd}")
    public User login(@Param("uid") String uid, @Param("pwd") String pwd);

    @Select("select * from user where uid = #{uid}")
    public User selectByUid(@Param("uid") String uid);

    @Insert("insert into user(uid,pwd,nick_name,state)" +
            "values (#{user.uid}, #{user.pwd}, #{user.nickName}, #{user.state})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    public int addUser(@Param("user") User user);
}
