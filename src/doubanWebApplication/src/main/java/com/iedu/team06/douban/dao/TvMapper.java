package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.Tv;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;


import java.util.List;

@Repository
public interface TvMapper {

    @Select("select * from sxy_douban_mivie limit 0, 30")
    public List<Tv> selectAll();

    @Select("<script>" +
            "SELECT id,tag,title,url,author,star5,star4,star3,star2,star1,type,time,short1,short2,short3" +
            "  FROM sxy_douban_mivie" +
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
            "  FROM sxy_douban_mivie" +
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
}
