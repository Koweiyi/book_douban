package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.Book;
import com.iedu.team06.douban.tools.BookScoreCount;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BookMapper {

    @Select("select * from books limit 0, 100")
    public List<Book> selectAll();

    @Select("select * from books where id = #{ID}")
    public Book selectById(@ Param("ID") String ID);

    @Select("select count(1) from books")
    public int bookCount();

    @Select("SELECT COUNT(DISTINCT(book_author)) FROM books;")
    public int authorCount();

    @Select("SELECT rate AS score, count(1) AS count\n" +
            "\tFROM `books` \n" +
            "\tWHERE rate <> \"\"\n" +
            "\tGROUP BY rate\n" +
            "\tORDER BY rate + 0 DESC;")
    public List<BookScoreCount> bookScoreCount();

    @Select("<script>" +
            "select id, book_name, book_author, publisher, date, price, page, tags, isbn, tags, rate" +
            "   from books" +
            "<where>" +
            "   <if test = 'book.bookName != null and book.bookName.length > 0'>" +
            "      and book_name like #{book.bookName}" +
            "   </if>" +
            "   <if test = 'book.bookAuthor != null and book.bookAuthor.length > 0'>" +
            "      and book_author like #{book.bookAuthor}" +
            "   </if>" +
            "   <if test = 'book.tags != null and book.tags.length > 0'>" +
            "      and tags like #{book.tags}" +
            "   </if>" +
            "   <if test = 'book.date != null and book.date.length > 0'>" +
            "      and date like #{book.date}" +
            "   </if>" +
            "   <if test = 'book.isbn != null and book.isbn.length > 0'>" +
            "      and isbn = #{book.isbn}" +
            "   </if>" +
            "</where>" +
            "<if test='start != null and limit != null'>" +
            "   limit #{start}, #{limit}" +
            "</if>" +
            "</script>")
    List<Book> selectByWhere(@Param("book") Book book, @Param("start") Integer start, @Param("limit") Integer limit);


    @Select("<script>" +
            "select count(1)" +
            "   from books" +
            "<where>" +
            "   <if test = 'book.bookName != null and book.bookName.length > 0'>" +
            "      and book_name like #{book.bookName}" +
            "   </if>" +
            "   <if test = 'book.bookAuthor != null and book.bookAuthor.length > 0'>" +
            "      and book_author like #{book.bookAuthor}" +
            "   </if>" +
            "   <if test = 'book.tags != null and book.tags.length > 0'>" +
            "      and tags like #{book.tags}" +
            "   </if>" +
            "   <if test = 'book.date != null and book.date.length > 0'>" +
            "      and date like #{book.date}" +
            "   </if>" +
            "   <if test = 'book.isbn != null and book.isbn.length > 0'>" +
            "      and isbn = #{book.isbn}" +
            "   </if>" +
            "</where>" +
            "   limit 0, 100" +
            "</script>")
    int countSelectByWhere(@Param("book") Book book);

    @Select("SELECT COUNT(DISTINCT(publisher)) FROM books")
    int punlisherCount();
}
