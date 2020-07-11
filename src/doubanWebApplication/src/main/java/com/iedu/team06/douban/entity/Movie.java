package com.iedu.team06.douban.entity;

import lombok.Data;

@Data
public class Movie {

    private String dbid;
    private String title;
    private String score;
    private String other_title;
    private String direct;
    private String country;
    private String movie_time;
    private String movie_type;
    private String vote_num;
    private String five_star;
    private String four_star;
    private String three_star;
    private String two_star;
    private String one_star;
    private String content;
    private String comment_time;
    private String comment_people;
    private String comment_star;
}
