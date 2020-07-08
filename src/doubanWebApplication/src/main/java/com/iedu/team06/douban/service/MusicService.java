package com.iedu.demo.demo.service;

import com.iedu.demo.demo.entity.Music;

import java.util.List;

public interface MusicService {

    /*User login(String uid, String pwd);*/

    /*Music addMusic(Music music);*/

    List<Music> search(Music music, int page, int limit);

    int searchCount(Music music);

    /*boolean resetPwd(int id);*/
}
