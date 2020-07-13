layui.use(['jquery','layer'],function () {

    let $ = layui.$,
        layer = layui.layer;
    let myChart = echarts.init(document.getElementById('tvcount'));
    let myChart2 = echarts.init(document.getElementById('tvcount2'));
    let myChart3 = echarts.init(document.getElementById('tvcount3'));
    let myChart4 = echarts.init(document.getElementById('tvcount4'));
    let myChart5 = echarts.init(document.getElementById('tvcount5'));
    $.post(
        "/logic/tv/count/scorecount",
        {},
        function (result) {
            console.log(result);
            let score = [];
            let count = [];
            let pieCount = [];

            //为图表组装数据
            for (i = 0;i < result.length;i++){

                if(i <= 10){
                    score.push(result[i].score);
                    count.push(result[i].count);
                }

                    //pieCount.push({'value':result[i].count,'name':result[i].score});
            }
            let option = {
                title: {
                    text: '电视剧分数分析'
                },
                tooltip: {},
                legend: {
                    data:['评分']
                },
                xAxis: {
                    data:score
                },
                yAxis: {},
                series: [{
                    name: '数量',
                    type: 'bar',
                    data: count
                }]
            };




            myChart.setOption(option);

        }
    )
    $.post(
        "/logic/tv/count/timecount",
        {},
        function (result) {
            console.log(result);
            let time = [];
            let count = [];
            let pieCount = [];

            //为图表组装数据
            for (i = 0;i < result.length;i++){

                if(i <= 10){
                    time.push(result[10-i].timecount);
                    count.push(result[10-i].count);
                }
                //pieCount.push({'value':result[i].count,'name':result[i].score});
            }
            let option2 = {
                title: {
                    text: '电影生产分布',
                    subtext: '豆瓣数据'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross'
                    }
                },
                toolbox: {
                    show: true,
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: time
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        formatter: '{value} 部'
                    },
                    axisPointer: {
                        snap: true
                    }
                },
                visualMap: {
                    show: false,
                    dimension: 0,
                    pieces: [{
                        lte: 8,
                        color: 'green'
                    }, {
                        gt: 8,
                        lte: 10,
                        color: 'red'
                    }]
                },
                series: [
                    {
                        name: '电影产量',
                        type: 'line',
                        smooth: true,
                        data: count,
                        markArea: {
                            data: [ [{
                                name: '高峰',
                                xAxis: '2018'
                            }, {
                                xAxis: '2020'
                            }] ]
                        }
                    }
                ]
            };
            myChart2.setOption(option2);
        }
    )
    let count5 = [];
    let count4 = [];
    let count3 = [];
    let count2 = [];
    let count1 = [];
    let x = [];
    for (i = -10;i < 100;i++){
        count5[i] = 0;
        count4[i] = 0;
        count3[i] = 0;
        count2[i] = 0;
        count1[i] = 0;
    }
    $.post(
        "/logic/tv/count/star5count",
        {},
        function (result) {
            //为图表组装数据
            for (i = 0;i < result.length;i++){
                count5[result[i].starcount5] = result[i].count;
            }
            console.log(count5);
        }
    )
    $.post(
        "/logic/tv/count/star4count",
        {},
        function (result) {

            //为图表组装数据
            for (i = 0;i < result.length;i++){
                count4[result[i].starcount4] = result[i].count;
            }
            console.log(count4);
        }
    )
    $.post(
        "/logic/tv/count/star3count",
        {},
        function (result) {

            //为图表组装数据
            for (i = 0;i < result.length;i++){
                count3[result[i].starcount3] = result[i].count;
            }
            console.log(count3);
        }
    )
    $.post(
        "/logic/tv/count/star2count",
        {},
        function (result) {
            //为图表组装数据
            for (i = 0;i < result.length;i++){
                count2[result[i].starcount2] = result[i].count;
            }
            console.log(count2);
        }
    )
    $.post(
        "/logic/tv/count/star1count",
        {},
        function (result) {

            //为图表组装数据
            for (i = 0;i < result.length;i++){
                count1[result[i].starcount1] = result[i].count;
            }
            console.log(count1);
            for(i = 0;i < 100;i++){
                x[i] = i;
            }
            let option3 = {
                title: {
                    text: '星级分布图'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['star5', 'star4', 'star3', 'star2', 'star1']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: x
                },
                yAxis: {
                    type: 'value'
                },

                series: [
                    {
                        name: 'star5',
                        type: 'line',
                        stack: '总量',
                        data: count1
                    },
                    {
                        name: 'star4',
                        type: 'line',
                        stack: '总量',
                        data: count2
                    },
                    {
                        name: 'star3',
                        type: 'line',
                        stack: '总量',
                        data: count3
                    },
                    {
                        name: 'star2',
                        type: 'line',
                        stack: '总量',
                        data: count4
                    },
                    {
                        name: 'star1',
                        type: 'line',
                        stack: '总量',
                        data: count5
                    }
                ]
            };


            myChart3.setOption(option3);
        }
    )





    $.post(
        "/logic/tv/count/tagcount",
        {},
        function (result) {
            console.log(result);
            let time = [];
            let count = [];
            let pieCount = [];

            //为图表组装数据
            for (i = 0;i < result.length;i++){

                if(i <= 10){
                    time.push(result[i].tag);
                    count.push(result[i].count);
                }
                //pieCount.push({'value':result[i].count,'name':result[i].score});
            }
            let option4 = {
                title: {
                    text: '类型分布',
                    subtext: '豆瓣数据'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross'
                    }
                },
                toolbox: {
                    show: true,
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: time
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        formatter: '{value} 部'
                    },
                    axisPointer: {
                        snap: true
                    }
                },
                visualMap: {
                    show: false,
                    dimension: 0,
                    pieces: [{
                        lte: 8,
                        color: 'green'
                    }, {
                        gt: 8,
                        lte: 10,
                        color: 'red'
                    }]
                },
                series: [
                    {
                        name: '电影产量',
                        type: 'line',
                        smooth: true,
                        data: count,
                        markArea: {
                            data: [ [{
                                name: '高峰',
                                xAxis: '2018'
                            }, {
                                xAxis: '2020'
                            }] ]
                        }
                    }
                ]
            };
            myChart4.setOption(option4);
        }
    )

    $.post(
        "/logic/tv/count/authorcount",
        {},
        function (result) {
            console.log(result);
            let time = [];
            let count = [];
            let pieCount = [];

            //为图表组装数据
            for (i = 0;i < result.length;i++){

                if(i <= 10){
                    time.push(result[i].author);
                    count.push(result[i].count);
                }
                //pieCount.push({'value':result[i].count,'name':result[i].score});
            }
            let option5 = {
                title: {
                    text: '导演影片生产量',
                    subtext: '豆瓣数据'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross'
                    }
                },
                toolbox: {
                    show: true,
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: time
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        formatter: '{value} 部'
                    },
                    axisPointer: {
                        snap: true
                    }
                },
                visualMap: {
                    show: false,
                    dimension: 0,
                    pieces: [{
                        lte: 8,
                        color: 'green'
                    }, {
                        gt: 8,
                        lte: 10,
                        color: 'red'
                    }]
                },
                series: [
                    {
                        name: '电影产量',
                        type: 'line',
                        smooth: true,
                        data: count,
                        markArea: {
                            data: [ [{
                                name: '高峰',
                                xAxis: '2018'
                            }, {
                                xAxis: '2020'
                            }] ]
                        }
                    }
                ]
            };
            myChart5.setOption(option5);
        }
    )



});