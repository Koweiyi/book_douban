package com.iedu.team06.douban.tools;

import lombok.Data;

@Data
public class LikeOrLooked {
    private String userUid;
    private String itemId;
    private int type;
}
