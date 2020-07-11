package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.Book;
import com.iedu.team06.douban.service.BookCountService;
import com.iedu.team06.douban.service.BookService;
import com.iedu.team06.douban.tools.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping("/logic/book")
public class BookController {

    @Autowired
    private BookService bookService;

    @Autowired
    private BookCountService bookCountSeivice;

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

    @RequestMapping(value = "/count/scoreCount")
    @ResponseBody
    public List<BookScoreCount> bookScoreCount(){
        return bookCountSeivice.scoreCount();
    }

    @RequestMapping(value = "/count/priceCount")
    @ResponseBody
    public List<DictElem> priceCount(){
        return  bookCountSeivice.priceCount();
    }

    @RequestMapping(value = "/count/allBookCount")
    @ResponseBody
    public CountMessage allBookCount(){
        CountMessage countMessage = new CountMessage();
        countMessage.setCount(bookCountSeivice.allBookCount());
        return countMessage;
    }

    @RequestMapping(value = "/count/authorCount")
    @ResponseBody
    public CountMessage authorCount(){
        CountMessage countMessage = new CountMessage();
        countMessage.setCount(bookCountSeivice.authorCount());
        return countMessage;
    }

    @RequestMapping(value = "/count/publisherCount")
    @ResponseBody
    public CountMessage publisherCount(){
        CountMessage countMessage = new CountMessage();
        countMessage.setCount(bookCountSeivice.publisherCount());
        return countMessage;
    }

    @RequestMapping(value = "/count/tagCount")
    @ResponseBody
    public List<ValueNameElem> tagCount(){
        return bookCountSeivice.tagCount();
    }

    @RequestMapping(value = "/count/publisherClassify")
    @ResponseBody
    public List<ValueNameElem> publisherClassify(){
        return  bookCountSeivice.publisherClassify();
    }

    @RequestMapping(value = "/count/dateClassify")
    @ResponseBody
    public List<ValueNameElem> dateClassify(){
        return bookCountSeivice.dateClassify();
    }

    @RequestMapping(value = "/count/authorClassify")
    @ResponseBody
    public List<ValueNameElem> authorClassify(){
        return bookCountSeivice.authorClassify();
    }

    @RequestMapping(value = "/count/starClassify")
    @ResponseBody
    public List<ValueNameElem> starClassify(){
        return bookCountSeivice.starClassify();
    }

    @RequestMapping("/{id}")
    @ResponseBody
    public BookDetail bookDetail(@PathVariable("id") int id){
        BookDetail bookDetail = new BookDetail();
        bookDetail.setBook(bookService.getBookById(id));
        bookDetail.setComments(bookService.getCommentsById(id));
        return bookDetail;
    }
}
