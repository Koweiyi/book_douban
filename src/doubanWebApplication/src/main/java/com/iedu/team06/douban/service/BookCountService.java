package com.iedu.team06.douban.service;

import com.iedu.team06.douban.tools.BookScoreCount;
import com.iedu.team06.douban.tools.DictElem;
import com.iedu.team06.douban.tools.ValueNameElem;

import java.util.List;

public interface BookCountService {
    public List<BookScoreCount> scoreCount();

    int allBookCount();

    int authorCount();

    int publisherCount();

    List<DictElem> priceCount();

    List<ValueNameElem> tagCount();

    List<ValueNameElem> publisherClassify();

    List<ValueNameElem> dateClassify();

    List<ValueNameElem> authorClassify();

    List<ValueNameElem> starClassify();
}
