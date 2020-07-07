package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.Tv;

import java.util.List;

public interface TvService {

    List<Tv> search2(Tv tv, int page, int limit);

    int search2Count(Tv tv);

}
