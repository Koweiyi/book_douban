package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.Tv;
import com.iedu.team06.douban.entity.TvsocreCount;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;


import java.util.List;

@Repository
public interface TvMapper {

    @Select("select * from sxy_douban_movie limit 0, 30")
    public List<Tv> selectAll();

    @Select("<script>" +
            "SELECT id,tag,rate,title,url,author,star5,star4,star3,star2,star1,type,time,short1,short2,short3" +
            "  FROM sxy_douban_movie" +
            "<where>" +
            "   <if test='tv.title != null and tv.title.length > 0'>" +
            "       AND title like #{tv,title}" +
            "   </if>" +
            "   <if test='tv.author != null and tv.author.length > 0'>" +
            "       AND author like '%${tv.author}%'" +
            "</if>" +
            "</where>" +
            "<if test='start != null and limit != null'>" +
            " limit #{start}, #{limit}" +
            "</if>" +
            "</script>" )
    public List<Tv> selectByWhere2(@Param("tv") Tv tv,
                                   @Param("start") Integer start ,
                                   @Param("limit") Integer limit);

    @Select("<script>" +
            "SELECT count(1)" +
            "  FROM sxy_douban_movie" +
            "<where>" +
            "   <if test='tv.title != null and tv.title.length > 0'>" +
            "       AND title like #{tv,title}" +
            "   </if>" +
            "   <if test='tv.author != null and tv.author.length > 0'>" +
            "       AND author like '%${tv.author}%'" +
            "   </if>" +
            "</where>" +
            "</script>")
    int countSelectByWhere2(@Param("tv") Tv tv);

    @Select(
            "SELECT rate AS score,COUNT(1) as count "+
            "FROM sxy_douban_movie " +
            "WHERE rate <> '' " +
            "GROUP BY rate " +
            "ORDER BY rate + 0 DESC" )
    public List<TvsocreCount> countByScore();

    @Select(
            "SELECT substring(time,1,4) AS timecount,COUNT(1) as count "+
                    "FROM sxy_douban_movie " +
                    "WHERE time <> '' " +
                    "GROUP BY timecount " +
                    "ORDER BY timecount + 0 DESC" )
    public List<TvsocreCount> countBytime();

    @Select(
            "SELECT substring(star5,1,2) AS starcount5,COUNT(1) as count " +
                "FROM sxy_douban_movie "  +
                    "WHERE star5 <> '' " +
            "GROUP BY starcount5 " +
            "ORDER BY starcount5 + 0 DESC " )
    public List<TvsocreCount> countBystar5();

    @Select(
            "SELECT substring(star4,1,2) AS starcount4,COUNT(1) as count " +
                    "FROM sxy_douban_movie "  +
                    "WHERE star4 <> '' " +
                    "GROUP BY starcount4 " +
                    "ORDER BY starcount4 + 0 DESC " )
    public List<TvsocreCount> countBystar4();

    @Select(
            "SELECT substring(star3,1,2) AS starcount3,COUNT(1) as count " +
                    "FROM sxy_douban_movie "  +
                    "WHERE star3 <> '' " +
                    "GROUP BY starcount3 " +
                    "ORDER BY starcount3 + 0 DESC " )
    public List<TvsocreCount> countBystar3();

    @Select(
            "SELECT substring(star2,1,2) AS starcount2,COUNT(1) as count " +
                    "FROM sxy_douban_movie "  +
                    "WHERE star2 <> '' " +
                    "GROUP BY starcount2 " +
                    "ORDER BY starcount2 + 0 DESC " )
    public List<TvsocreCount> countBystar2();

    @Select(
            "SELECT substring(star1,1,2) AS starcount1,COUNT(1) as count " +
                    "FROM sxy_douban_movie "  +
                    "WHERE star1 <> '' " +
                    "GROUP BY starcount1 " +
                    "ORDER BY starcount1 + 0 DESC " )
    public List<TvsocreCount> countBystar1();

    @Select(
            "SELECT tag AS tag,COUNT(1) as count " +
                    "FROM sxy_douban_movie "  +
                    "WHERE tag <> '' " +
                    "GROUP BY tag " +
                    "ORDER BY tag + 0 DESC " )
    public List<TvsocreCount> countBytag();

    @Select(
            "SELECT author AS author,COUNT(1) as count " +
                    "FROM sxy_douban_movie "  +
                    "WHERE author <> '' " +
                    "GROUP BY author " +
                    "ORDER BY COUNT(1) + 0 DESC " )
    public List<TvsocreCount> countByauthor();

}
