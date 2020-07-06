package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.Book;
import com.iedu.team06.douban.service.BookService;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping("/logic/book")
public class BookController {

    @Autowired
    private BookService bookService;

    @RequestMapping(value = "/search")
    @ResponseBody
    public TableData search(Book book, int page, int limit){
        TableData tableData = new TableData() ;
        List<Book> result = bookService.search(book, page, limit);

        tableData.setCode(0);
        tableData.setMsg("");
        tableData.setCount(bookService.searchCount(book));
        tableData.setData(result);

        return tableData;
    }

}
