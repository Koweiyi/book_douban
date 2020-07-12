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

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Controller
@RequestMapping("/logic/book")
public class BookController {

    @Autowired
    private BookService bookService;

    @Autowired
    private BookCountService bookCountSeivice;

    private static final DateTimeFormatter TIME_FORMAT = DateTimeFormatter.ofPattern("yyyy-MM-dd");

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
    public BookDetail bookDetail(@PathVariable("id") int id, String uid){
        BookDetail bookDetail = new BookDetail();
        bookDetail.setBook(bookService.getBookById(id));
        bookDetail.setComments(bookService.getCommentsById(id));
        bookDetail.setMyComment(bookService.getMyComment(id, uid));
        return bookDetail;
    }

    @RequestMapping(value = "/edit")
    @ResponseBody
    public Message bookEdit(String rate, int like, int looked, String comment, String userUid, String itemId){
        Message message = new Message();
        if(userUid == null){
            message.setError(true);
            message.setContent("您当前尚未登录，请登录后进行编辑操作");
            return message;
        }
        try{
            if(like == 1){
                bookService.addLike(userUid, itemId, 1);
            }else{
                bookService.removeLike(userUid, itemId, 1);
            }
            if(looked == 1){
                bookService.addLooked(userUid, itemId, 1);
            }else{
                bookService.removeLooked(userUid, itemId, 1);
            }
            if(!"".equals(message)){
                bookService.addComment(itemId, userUid, comment, TIME_FORMAT.format(LocalDateTime.now()), rate);
            }
        }
        catch (Exception e){
            e.printStackTrace();
            message.setError(true);
            message.setContent("服务器错误，编辑失败！请重新尝试。");
            return message;
        }

        message.setError(false);
        return message;
    }
}
