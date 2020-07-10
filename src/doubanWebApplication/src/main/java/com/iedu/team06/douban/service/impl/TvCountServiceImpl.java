package com.iedu.team06.douban.service.impl;

import com.iedu.team06.douban.dao.TvMapper;
import com.iedu.team06.douban.entity.TvsocreCount;
import com.iedu.team06.douban.service.TvCountService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TvCountServiceImpl implements TvCountService {
    @Autowired
    private TvMapper tvMapper;

    @Override
    public List<TvsocreCount> scoreCount(){
        //return tvMapper.countByScore();
        return null;
    }
}
