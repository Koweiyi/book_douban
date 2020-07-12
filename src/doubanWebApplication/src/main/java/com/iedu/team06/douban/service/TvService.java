package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.Tv;
import com.iedu.team06.douban.entity.TvsocreCount;
import com.iedu.team06.douban.entity.Tvtimecount;

import java.util.List;

public interface TvService {

    List<Tv> search2(Tv tv, int page, int limit);

    int search2Count(Tv tv);

    public List<TvsocreCount> scoreCount();

    public List<Tvtimecount> timeCount();

}
