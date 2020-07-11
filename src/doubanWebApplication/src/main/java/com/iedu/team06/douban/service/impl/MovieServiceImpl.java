package com.iedu.team06.douban.service.impl;


import com.iedu.team06.douban.dao.MovieMapper;
import com.iedu.team06.douban.entity.Movie;
import com.iedu.team06.douban.service.MovieService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MovieServiceImpl implements MovieService {

    @Autowired
    private MovieMapper mapper;

    @Override
    public List<Movie> search_movie(Movie movie,int page,int limit){

        if(movie != null && !"".equals(movie.getDirect().trim())) {
            movie.setDirect("%" + movie.getDirect() + "%");
        }

        if(movie != null && !"".equals(movie.getCountry().trim())) {
            movie.setCountry("%" + movie.getCountry() + "%");
        }

        if(page > 0 && limit > 0)
            return mapper.selectByWhere(movie,(page - 1) * limit, limit);

        return mapper.selectByWhere(movie,null,null);
    }

    @Override
    public int searchCount(Movie movie){
        return mapper.countSelectByWhere(movie);
    }
}
