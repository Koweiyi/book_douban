package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.User;
import com.iedu.team06.douban.tools.EditUserData;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserMapper {

    @Select("select * from user limit 0, 30")
    public List<User> selectAll();

    @Select("select id, uid, nick_name, state from user where uid = #{uid} and pwd = #{pwd}")
    public User login(@Param("uid") String uid, @Param("pwd") String pwd);

    @Select("select * from user where uid = #{uid}")
    public User selectByUid(@Param("uid") String uid);

    @Insert("insert into user(uid,pwd,nick_name,state)" +
            "values (#{user.uid}, #{user.pwd}, #{user.nickName}, #{user.state})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    public int addUser(@Param("user") User user);

    @Update("update user set uid = #{edit.newUid}, pwd = #{edit.newPwd}, nick_name = #{edit.newNickName} where id = #{edit.id}")
    int editByID(@Param("edit") EditUserData editUserData);

    @Update("update user" +
            "   set uid = #{user.uid}" +
            "       pwd = #{user.pwd}" +
            "       nick_name = #{user.nickName}" +
            "       state = #{user.state}" +
            "   where id = #{user.id}")
    int update(@Param("user") User oldUser);
}
