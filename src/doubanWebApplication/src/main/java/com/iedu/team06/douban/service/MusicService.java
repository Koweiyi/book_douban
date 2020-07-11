package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.Music;
import com.iedu.team06.douban.entity.MusicscoreCount;
import com.iedu.team06.douban.entity.MusicusersiteCount;

import java.util.List;

public interface MusicService {

    /*User login(String uid, String pwd);*/

    /*Music addMusic(Music music);*/

    List<Music> search(Music music, int page, int limit);

    List<MusicscoreCount> scoreCount();

    List<MusicusersiteCount> siteCount();

    int searchCount(Music music);

    /*boolean resetPwd(int id);*/
}
