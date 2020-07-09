package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.User;
import com.iedu.team06.douban.tools.EditUserData;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserMapper {

    @Select("select id, uid, nick_name, state from user")
    public List<User> selectAll();

    @Select("select id, uid, nick_name, state,profile_url from user where uid = #{uid} and pwd = #{pwd}")
    public User login(@Param("uid") String uid, @Param("pwd") String pwd);

    @Select("select * from user where id = #{id}")
    public User selectById(@Param("id") String id);

    @Select("select * from user where uid = #{uid}")
    public User selectByUid(@Param("uid") String uid);

    @Insert("insert into user(uid,pwd,nick_name,state)" +
            "values (#{user.uid}, #{user.pwd}, #{user.nickName}, #{user.state})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    public int addUser(@Param("user") User user);

    @Update("update user set uid = #{edit.newUid}, pwd = #{edit.newPwd}, nick_name = #{edit.newNickName} where id = #{edit.id}")
    int editByID(@Param("edit") EditUserData editUserData);

    @Update("update user" +
            "   set uid = #{user.uid}," +
            "       pwd = #{user.pwd}," +
            "       nick_name = #{user.nickName}," +
            "       state = #{user.state}," +
            "       profile_url = #{user.profileUrl}" +
            "   where id = #{user.id}")
    int update(@Param("user") User user);

    @Select("<script>"+
            "SELECT id, uid, nick_name, state " +
            "FROM user" +
            "<where>"+
            "<if test='user.uid != null and user.uid. length > 0'>" +
            "AND uid like #{user.uid}" +
            "   </if>" +
            "   <if test='user.nickName != null and user.nickName.length > 0'>" +
            "       AND nick_name like #{user.nickName }" +
            "   </if>" +
            "   <if test= 'user.state != null and user.state != -1' >" +
            "       AND state = #{user.state}" +
            "   </if>" +
            "</where>" +
            "   <if test='start != null and limit != null'>" +
            "       limit #{start}, #{limit}" +
            "   </if>" +
            "</script>" )
    public List<User> selectByWhere ( @Param("user") User user ,
                                      @Param("start") Integer start ,
                                      @Param("limit") Integer limit);

    @Select("<script>" +
            "SELECT count(1)" +
            "   FROM user" +
            "<where>" +
            "   <if test='user.uid != null and user.uid.length > 0'>"+
            "       AND uid like #{user.uid}" +
            "   </if>" +
            "   <if test= 'user.nickName != null and user.nickName.length > 0'>" +
            "       AND nick_name like #{user.nickName}" +
            "   </if>" +
            "   <if test= 'user.state != null and user.state != - 1' >" +
            "       AND state = #{user.state}" +
            "   </if>" +
            "</where>" +
            "</script>")
    int countSelectByWhere (@Param("user") User user);
}
