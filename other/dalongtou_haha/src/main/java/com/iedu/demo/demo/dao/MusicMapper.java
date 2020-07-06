package com.iedu.demo.demo.dao;

import com.iedu.demo.demo.entity.Music;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MusicMapper {

    @Select("select * from dalongtou_music limit 0, 30")
    public List<Music> selectAll();

    /*@Select("select * from user where uid = #{uid} and pwd = #{pwd} and state = 1")
    public Music login(@Param("uid") String uid, @Param("pwd") String pwd);*/

    @Select("select * from dalongtou_music where music_name = #{m_name}")
    public Music seceltByM_name(@Param("m_name") String m_name);

    /*@Insert("insert into dalongtou_music(uid,pwd,nick_name,state) " +
            "   values(#{user.uid},#{user.pwd},#{user.nickName},#{user.state})")
    @Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
    public int addUser(@Param("user") Music user);*/

    /*@Update("update dalongtou_music set pwd = #{newPwd} where id = #{id}")
    int updatePwd(@Param("id") int id, @Param("newPwd") String newPwd);*/

    @Select("select id, music_name, music_man, music_mark from dalongtou_music where id = #{id}")
    public Music selectById(@Param("id") int id);

    @Select("<script>"+
            "SELECT id, music_name, music_man, music_mark " +
            "FROM dalongtou_music" +
            "<where>"+
            "   <if test='music.m_name != null and music.m_name.length > 0'>" +
            "       AND music_name like #{music.m_name}" +
            "   </if>" +
            "   <if test='music.m_man != null and music.m_man.length > 0'>" +
            "       AND music_man like #{music.m_man}" +
            "   </if>" +
            "   <if test= 'music.m_mark != null and music.m_mark != -1' >" +
            "       AND music_mark = #{music.m_mark}" +
            "   </if>" +
            "</where>" +
            "   <if test='start != null and limit != null'>" +
            "       limit #{start}, #{limit}" +
            "   </if>" +
            "</script>" )
    public List<Music> selectByWhere ( @Param("music") Music music ,
                                      @Param("start") Integer start ,
                                      @Param("limit") Integer limit);

    @Select("<script>" +
            "SELECT count(1)" +
            "   FROM dalongtou_music" +
            "<where>" +
            "   <if test='music.m_name != null and music.m_name.length > 0'>" +
            "       AND music_name like #{music.m_name}" +
            "   </if>" +
            "   <if test='music.m_man != null and music.m_man.length > 0'>" +
            "       AND music_man like #{music.m_man}" +
            "   </if>" +
            "   <if test= 'music.m_mark != null and music.m_mark != -1' >" +
            "       AND music_mark = #{music.m_mark}" +
            "   </if>" +
            "</where>" +
            "</script>")
    int countSelectByWhere (@Param("music") Music music);
}
