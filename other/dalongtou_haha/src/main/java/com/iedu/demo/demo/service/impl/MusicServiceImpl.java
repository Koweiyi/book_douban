package com.iedu.demo.demo.service.impl;

import com.iedu.demo.demo.dao.MusicMapper;
import com.iedu.demo.demo.entity.Music;
import com.iedu.demo.demo.service.MusicService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MusicServiceImpl implements MusicService {

    @Autowired
    private MusicMapper mapper;

    /*@Override
    public User login(String uid, String pwd){

        User user = mapper.login(uid,pwd);
        if (user != null && user.getState() == 1)
            return user;
        return null;

    }*/
    /*@Override
    public Music addMusic(Music music){
        if (mapper.seceltByM_name(music.getM_name())==null){
            music.setM_mark("0");
            mapper.addMusic(music);
            return music;
        }
        return null;
    }*/

    @Override
    public List<Music> search(Music music, int page, int limit) {

        if(music != null && !"".equals(music.getM_name().trim())) {
            music.setM_name("%" + music.getM_name() + "%");
        }

        if(page > 0 && limit > 0)
            return mapper.selectByWhere(music,(page - 1) * limit, limit);

        return mapper.selectByWhere(music,null,null);


    }
    @Override
    public int searchCount(Music music){
        return mapper.countSelectByWhere(music);
    }

    /*@Override
    public boolean resetPwd(int id){
        String defaultPwd = "000000";

        if(mapper.updatePwd(id,defaultPwd)==1)
            return true;
        return false;
    }*/
}
