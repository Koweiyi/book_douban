package com.iedu.team06.douban.entity;

import lombok.Data;

@Data
public class Book {
    private String ID;
    private String bookName;
    private String bookAuthor;
    private String publisher;
    private String data;
    private String price;
    private String tags;
    private String intro;
    private String rate;
    private String ratePl;
    private String fiveStar;
    private String fourStar;
    private String threeStar;
    private String twoStar;
    private String oneStar;
}
