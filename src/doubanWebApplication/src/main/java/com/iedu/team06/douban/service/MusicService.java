package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.Music;

import java.util.List;

public interface MusicService {

    /*User login(String uid, String pwd);*/

    /*Music addMusic(Music music);*/

    List<Music> search(Music music, int page, int limit);

    int searchCount(Music music);

    /*boolean resetPwd(int id);*/
}
