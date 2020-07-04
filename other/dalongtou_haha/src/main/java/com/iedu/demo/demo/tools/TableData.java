package com.iedu.demo.demo.tools;

import lombok.Data;

import java.util.List;

@Data
public class TableData {

    private int code;
    private String msg;
    private int count;
    private List<? extends Object> data;
}
