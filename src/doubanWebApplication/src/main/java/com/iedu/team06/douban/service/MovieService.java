package com.iedu.team06.douban.service;

import com.iedu.team06.douban.entity.Movie;

import java.util.List;


public interface MovieService {
    List<Movie> search_movie(Movie movie, int page, int limit);

    int searchCount(Movie movie);
}
