package com.iedu.team06.douban.controller;

import com.iedu.team06.douban.entity.Tv;
import com.iedu.team06.douban.entity.TvsocreCount;
import com.iedu.team06.douban.service.TvCountService;
import com.iedu.team06.douban.tools.TableData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
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

    @Autowired
    private TvCountService countService;

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
    public List<TvsocreCount> scoreCount(){
        return countService.scoreCount();
    }


}
