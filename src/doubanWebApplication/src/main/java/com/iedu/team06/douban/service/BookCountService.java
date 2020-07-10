package com.iedu.team06.douban.service;

import com.iedu.team06.douban.tools.BookScoreCount;

import java.util.List;

public interface BookCountService {
    public List<BookScoreCount> scoreCount();

    int allBookCount();

    int authorCount();

    int publisherCount();
}
