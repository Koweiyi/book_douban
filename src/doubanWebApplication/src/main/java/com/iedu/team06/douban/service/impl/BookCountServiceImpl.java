package com.iedu.team06.douban.service.impl;

import com.iedu.team06.douban.dao.BookMapper;
import com.iedu.team06.douban.service.BookCountService;
import com.iedu.team06.douban.tools.BookScoreCount;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookCountServiceImpl implements BookCountService {

    @Autowired
    private BookMapper mapper;

    @Override
    public List<BookScoreCount> scoreCount() {
        return mapper.bookScoreCount();
    }

    @Override
    public int allBookCount() {
        return mapper.bookCount();
    }

    @Override
    public int authorCount() {
        return mapper.authorCount();
    }

    @Override
    public int publisherCount() {
        return mapper.punlisherCount();
    }
}
