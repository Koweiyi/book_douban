package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.Music;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MusicMapper {

    @Select("select * from dalongtou_music ")
    public List<Music> selectAll();

    @Select("<script>" + "select music_id, music_name, music_rename, music_man, music_sect," +
            "music_album, music_media, music_time, music_mark, music_vote, music_star5," +
            "music_star4, music_star3, music_star2, music_star1, music_url " +
            " from dalongtou_music " +
            "<where>" +
            "   <if test='music.musicName != null and music.musicName.length > 0'>" +
            "       and music_name like #{music.musicName}" +
            "   </if>" +
            "   <if test='music.musicMan != null and music.musicMan.length > 0'>" +
            "       and music_man like #{music.musicMan}" +
            "   </if>" +
            "   <if test= 'music.musicMark != null and music.musicMark.length > 0'>" +
            "       and music_mark = #{music.musicMark}" +
            "   </if>" +
            "</where>" +
            "   <if test='start != null and limit != null'>" +
            "       limit #{start}, #{limit}" +
            "   </if>" +
            "</script>")
    public List<Music> selectByWhere(@Param("music") Music music,
                                     @Param("start") Integer start,
                                     @Param("limit") Integer limit);

    @Select("<script>" +
            "select count(1)" +
            "   from dalongtou_music " +
            "<where>" +
            "   <if test='music.musicName != null and music.musicName.length > 0'>" +
            "       and music_name like #{music.musicName}" +
            "   </if>" +
            "   <if test='music.musicMan != null and music.musicMan.length > 0'>" +
            "       and music_man like #{music.musicMan}" +
            "   </if>" +
            "   <if test= 'music.musicMark != null' >" +
            "       and music_mark = #{music.musicMark}" +
            "   </if>" +
            "</where>" +
            "</script>")
    int countSelectByWhere(@Param("music") Music music);
}
