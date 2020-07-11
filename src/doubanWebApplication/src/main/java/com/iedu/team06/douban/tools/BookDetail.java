package com.iedu.team06.douban.tools;

import com.iedu.team06.douban.entity.Book;
import lombok.Data;

import java.util.List;

@Data
public class BookDetail {
    Book book;
    List<Comment> comments;
}
