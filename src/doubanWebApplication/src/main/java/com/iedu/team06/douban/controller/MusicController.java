package com.iedu.team06.douban.controller;


import com.iedu.team06.douban.service.MusicService;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import com.iedu.team06.douban.entity.Music;

import java.util.List;

@Controller
@RequestMapping("/logic/music")
public class MusicController {

    @Autowired
    private MusicService musicService;


    @RequestMapping(value="/search2")
    @ResponseBody
    public TableData search2(Music music, int page, int limit) {

        TableData date = new TableData();
        List<Music> result = musicService.search(music, page, limit);
        date.setCode(0);
        date.setMsg("");
        date.setCount(musicService.searchCount(music));
        date.setData(result);

        return date;
    }
}
