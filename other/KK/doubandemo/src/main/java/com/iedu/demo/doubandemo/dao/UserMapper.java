package com.iedu.demo.doubandemo.dao;

import com.iedu.demo.doubandemo.entity.User;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserMapper {

    @Select("select * from user")
    public List<User> selectAll();
}
