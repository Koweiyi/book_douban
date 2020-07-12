package com.iedu.team06.douban.service.impl;

import com.iedu.team06.douban.dao.BookMapper;
import com.iedu.team06.douban.entity.Book;
import com.iedu.team06.douban.service.BookService;
import com.iedu.team06.douban.tools.Comment;
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
            if (!"".equals(book.getDate().trim()))
                book.setDate("%" + book.getDate() + "%");
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

    @Override
    public Book getBookById(int id) {
        return bookMapper.getBookById(id);
    }

    @Override
    public List<Comment> getCommentsById(int id) {
        return bookMapper.getCommentsById(id);
    }

    @Override
    public void addLike(String userUid, String itemId, int i) {
        if(bookMapper.selectLike(userUid,itemId) == null)
            bookMapper.addLike(userUid, itemId, i);
    }

    @Override
    public void removeLike(String userUid, String itemId, int i) {
        bookMapper.removeLike(userUid, itemId, i);
    }

    @Override
    public void removeLooked(String userUid, String itemId, int i) {
        bookMapper.removeLooked(userUid, itemId, i);
    }

    @Override
    public void addLooked(String userUid, String itemId, int i) {
        if (bookMapper.selectLooked(userUid, itemId) == null)
            bookMapper.addLooked(userUid, itemId, i);
    }

    @Override
    public void addComment(String itemId, String userUid, String comment, String format, String rate) {
        if(bookMapper.selectComment(itemId, userUid, format) == null)
            bookMapper.addComment(itemId, userUid, comment, format, rate);
    }

}
