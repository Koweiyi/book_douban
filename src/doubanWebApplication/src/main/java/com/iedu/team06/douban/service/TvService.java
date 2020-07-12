package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.Tv;
import com.iedu.team06.douban.entity.TvsocreCount;

import java.util.List;

public interface TvService {

    List<Tv> search2(Tv tv, int page, int limit);

    int search2Count(Tv tv);

    public List<TvsocreCount> scoreCount();

    public List<TvsocreCount> timeCount();

    public List<TvsocreCount> star5Count();

    public List<TvsocreCount> star4Count();

    public List<TvsocreCount> star3Count();

    public List<TvsocreCount> star2Count();

    public List<TvsocreCount> star1Count();

    public List<TvsocreCount> tagCount();

    public List<TvsocreCount> authorCount();
}
