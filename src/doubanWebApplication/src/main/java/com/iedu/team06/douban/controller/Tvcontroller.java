package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.Tv;
import com.iedu.team06.douban.entity.TvsocreCount;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import com.iedu.team06.douban.service.TvService;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.SessionAttributes;

import java.util.List;

@RestController
@RequestMapping("/logic/tv")
@SessionAttributes
public class Tvcontroller {
    @Autowired
    private  TvService service;


    @RequestMapping(value="/search2")
    @ResponseBody
    public TableData search2(Tv tv, int page, int limit) {
        TableData date = new TableData();
        List<Tv> result = service.search2(tv,page,limit);
        date.setCode(0);
        date.setMsg("");
        date.setCount(service.search2Count(tv));
        date.setData(result);

        return date;
    }

    @RequestMapping(value = "/count/scorecount")
    public List<TvsocreCount> scoreCount(){ return service.scoreCount(); }

    @RequestMapping(value = "/count/timecount")
    public List<TvsocreCount> timeCount(){ return service.timeCount(); }

    @RequestMapping(value = "/count/star5count")
    public List<TvsocreCount> star5Count(){ return service.star5Count(); }

    @RequestMapping(value = "/count/star4count")
    public List<TvsocreCount> star4Count(){ return service.star4Count(); }

    @RequestMapping(value = "/count/star3count")
    public List<TvsocreCount> star3Count(){ return service.star3Count(); }

    @RequestMapping(value = "/count/star2count")
    public List<TvsocreCount> star2Count(){ return service.star2Count(); }

    @RequestMapping(value = "/count/star1count")
    public List<TvsocreCount> star1Count(){ return service.star1Count(); }

    @RequestMapping(value = "/count/tagcount")
    public List<TvsocreCount> tagCount(){ return service.tagCount(); }

    @RequestMapping(value = "/count/authorcount")
    public List<TvsocreCount> authorCount(){ return service.authorCount(); }
}
