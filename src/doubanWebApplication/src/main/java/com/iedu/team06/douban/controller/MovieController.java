package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.Movie;
import com.iedu.team06.douban.service.MovieService;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping("/logic/movie")
public class MovieController {

    @Autowired
    private MovieService movieService;

    @RequestMapping(value = "/search_movie")
    @ResponseBody
    public TableData search_movie(Movie movie, int page, int limit){
        TableData date = new TableData();
        List<Movie> result = movieService.search_movie(movie, page, limit);

        date.setCode(0);
        date.setMsg("");
        date.setCount(movieService.searchCount(movie));
        date.setData(result);

        return date;
    }

}
