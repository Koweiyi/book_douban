package com.iedu.team06.douban.dao;

import com.iedu.team06.douban.entity.Book;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BookMapper {

    @Select("select * from books limit 0, 100")
    public List<Book> selectAll();

    @Select("select * from books where ID = #{ID}")
    public Book selectById(String ID);


}
