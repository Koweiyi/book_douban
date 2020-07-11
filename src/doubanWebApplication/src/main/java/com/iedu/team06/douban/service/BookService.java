package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.Book;
import com.iedu.team06.douban.tools.Comment;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface BookService {
    List<Book> search(Book book, int page, int limit);

    int searchCount(Book book);

    Book getBookById(int id);

    List<Comment> getCommentsById(int id);
}
