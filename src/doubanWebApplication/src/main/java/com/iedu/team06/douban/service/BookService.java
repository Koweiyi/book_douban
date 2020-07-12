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

    void addLike(String userUid, String itemId, int i);

    void removeLike(String userUid, String itemId, int i);

    void removeLooked(String userUid, String itemId, int i);

    void addLooked(String userUid, String itemId, int i);

    void addComment(String itemId, String userUid, String comment, String format, String rate);

    Comment getMyComment(int id, String uid);
}
