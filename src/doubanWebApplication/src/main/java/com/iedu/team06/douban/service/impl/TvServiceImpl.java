package com.iedu.team06.douban.service.impl;

import com.iedu.team06.douban.entity.Tv;
import com.iedu.team06.douban.entity.TvsocreCount;
import com.iedu.team06.douban.service.TvService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.iedu.team06.douban.dao.TvMapper;

import java.util.List;

@Service
public class TvServiceImpl implements TvService {

    @Autowired
    private TvMapper mapper;

    @Override
    public List<Tv> search2(Tv tv, int page, int limit) {
        if (tv != null && !"".equals(tv.getTitle().trim())) {
            tv.setTitle("%" + tv.getTitle() + "%");
        }
        if (page > 0 && limit > 0)
            return mapper.selectByWhere2(tv, (page-1) * limit, limit);
        return mapper.selectByWhere2(tv, null, null);
    }

    @Override
    public int search2Count(Tv tv) {

        return mapper.countSelectByWhere2(tv);
    }

    @Override
    public List<TvsocreCount> scoreCount(){
        return mapper.countByScore();
    }


    @Override
    public List<TvsocreCount> timeCount(){
        return mapper.countBytime();

    }

    @Override
    public List<TvsocreCount> star5Count(){
        return mapper.countBystar5();

    }

    @Override
    public List<TvsocreCount> star4Count(){
        return mapper.countBystar4();

    }

    @Override
    public List<TvsocreCount> star3Count(){
        return mapper.countBystar3();

    }

    @Override
    public List<TvsocreCount> star2Count(){
        return mapper.countBystar2();

    }

    @Override
    public List<TvsocreCount> star1Count(){
        return mapper.countBystar1();

    }

    @Override
    public List<TvsocreCount> tagCount(){
        return mapper.countBytag();

    }

    @Override
    public List<TvsocreCount> authorCount(){
        return mapper.countByauthor();

    }
}
