package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.Movie;
import org.apache.ibatis.annotations.*;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MovieMapper {

    @Select("select * from hzc_movie_detail")
    public List<Movie> selectAll();

    @Select("<script>" + "select dbid, other_title, direct, country,"+
            "movie_time, movie_type, vote_num,"+
            "five_star, four_star, three_star, two_star, one_star"+
            "from hzc_movie_detail" +
            "<where>"+
            "<if test='movie.direct != null and movie.direct.length > 0'>"+
            "       and direct like #{movie.direct}" +
            "   </if>" +
            "   <if test='movie.country != null and movie.country.length > 0'>" +
            "       and country like #{movie.country}" +
            "   </if>" +
            "   <if test= 'movie.dbid != null and movie.dbid.length > 0'>" +
            "       and dbid = #{movie.dbid}" +
            "   </if>" +
            "</where>" +
            "   <if test='start != null and limit != null'>" +
            "       limit #{start}, #{limit}" +
            "   </if>" +
            "</script>")
    public List<Movie> selectByWhere(@Param("movie") Movie movie,
                                     @Param("start") Integer start,
                                     @Param("limit") Integer limit);

    @Select("<script>" +
            "select count(1)" +
            "   from hzc_movie_detail " +
            "<where>" +
            "   <if test='movie.direct != null and movie.direct.length > 0'>" +
            "       and direct like #{movie.direct}" +
            "   </if>" +
            "   <if test='movie.country != null and movie.country.length > 0'>" +
            "       and country like #{movie.country}" +
            "   </if>" +
            "   <if test= 'music.dbid != null' >" +
            "       and dbid = #{movie.dbid}" +
            "   </if>" +
            "</where>" +
            "</script>")
    int countSelectByWhere(@Param("movie") Movie movie);
}

