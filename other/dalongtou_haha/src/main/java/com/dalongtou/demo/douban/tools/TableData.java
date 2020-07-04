package com.dalongtou.demo.douban.tools;

import com.dalongtou.demo.douban.entity.User;
import lombok.Data;

import java.util.List;

@Data
public class TableData {

    private int code;
    private String msg;
    private int count;
    private List<? extends Object> data;

}
