package com.dalongtou.demo.douban.dao;

import com.dalongtou.demo.douban.entity.User;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserMapper {

    @Select("select * from user")
    public List<User> selectAll();

}
