package com.iedu.team06.douban.service.impl;

import com.iedu.team06.douban.dao.MusicMapper;
import com.iedu.team06.douban.entity.Music;
import com.iedu.team06.douban.entity.MusicscoreCount;
import com.iedu.team06.douban.entity.MusicusersiteCount;
import com.iedu.team06.douban.service.MusicService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MusicServiceImpl implements MusicService {

    @Autowired
    private MusicMapper mapper;


    @Override
    public List<Music> search(Music music, int page, int limit) {

        if(music != null && !"".equals(music.getMusicName().trim())) {
            music.setMusicName("%" + music.getMusicName() + "%");
        }

        if(music != null && !"".equals(music.getMusicMan().trim())) {
            music.setMusicMan("%" + music.getMusicMan() + "%");
        }

        /*if(music != null && !"".equals(music.getmusicmark().trim())) {
            music.setmusicmark("%" + music.getmusicmark() + "%");
        }*/

        if(page > 0 && limit > 0)
            return mapper.selectByWhere(music,(page - 1) * limit, limit);

        return mapper.selectByWhere(music,null,null);


    }
    @Override
    public int searchCount(Music music){
        return mapper.countSelectByWhere(music);
    }

    @Override
    public List<MusicscoreCount> scoreCount(){

        return mapper.countByScore();

    }

    @Override
    public List<MusicscoreCount> sectCount(){

        return mapper.countBySect();

    }

    @Override
    public List<MusicscoreCount> manCount(){

        return mapper.countByMan();

    }

    @Override
    public List<MusicusersiteCount> siteCount(){

        return mapper.countBysite();

    }

}
