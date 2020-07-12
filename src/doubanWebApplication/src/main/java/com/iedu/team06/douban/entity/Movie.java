package com.iedu.team06.douban.entity;

import lombok.Data;

@Data
public class Movie {

    private String dbid;
    private String title;
    private String score;
    private String otherTitle;
    private String direct;
    private String country;
    private String movieTime;
    private String movieType;
    private String voteNum;
    private String fiveStar;
    private String fourStar;
    private String threeStar;
    private String twoStar;
    private String oneStar;
    private String content;
    private String comment_time;
    private String comment_people;
    private String comment_star;
}
