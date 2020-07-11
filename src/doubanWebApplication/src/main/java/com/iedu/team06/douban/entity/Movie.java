package com.iedu.team06.douban.entity;

import lombok.Data;

@Data
public class Movie {

    private String dbid;
    private String title;
    private String score;
    private String other_title;
    private String direct;
}
