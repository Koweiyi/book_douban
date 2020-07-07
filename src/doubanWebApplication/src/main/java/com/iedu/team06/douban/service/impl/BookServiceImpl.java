package com.iedu.team06.douban.service.impl;

import com.iedu.team06.douban.dao.BookMapper;
import com.iedu.team06.douban.entity.Book;
import com.iedu.team06.douban.service.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookServiceImpl implements BookService {

    @Autowired
    private BookMapper bookMapper;

    @Override
    public List<Book> search(Book book, int page, int limit) {

//        return bookMapper.selectAll();

        if(book != null){
            if(!"".equals(book.getBookName().trim()))
                book.setBookName("%" + book.getBookName() + "%");
            if(!"".equals(book.getBookAuthor().trim()))
                book.setBookAuthor("%" + book.getBookAuthor() + "%");
            if(!"".equals(book.getTags().trim()))
                book.setTags("%" + book.getTags() + "%");
//            if (!"".equals(book.getDate().trim()))
//                book.setDate("%" + book.getDate() + "%");
        }

        if (page > 0 && limit > 0)
            return bookMapper.selectByWhere(book, (page - 1) * limit, limit);

        return bookMapper.selectByWhere(book, null, null);
    }

    @Override
    public int searchCount(Book book) {
//        int res = bookMapper.countSelectByWhere(book);
//        return  res > 100 ? 100 : res;
        return bookMapper.countSelectByWhere(book);
    }
}
