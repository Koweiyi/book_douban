package com.iedu.team06.douban.tools;

import lombok.Data;

@Data
public class EditUserData {

    private String id;
    private String oldPwd;
    private String newUid;
    private String newPwd;
    private String newNickName;

}
