layui.use(['jquery','layer'],function () {

    let $ = layui.$,
        layer = layui.layer;
    let myChart = echarts.init(document.getElementById('tvcount'));
    let myChart2 = echarts.init(document.getElementById('tvcount2'));
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
                    data: ['00:00', '01:15', '02:30', '03:45', '05:00', '06:15', '07:30', '08:45', '10:00', '11:15', '12:30', '13:45', '15:00', '16:15', '17:30', '18:45', '20:00', '21:15', '22:30', '23:45']
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        formatter: '{value} W'
                    },
                    axisPointer: {
                        snap: true
                    }
                },
                visualMap: {
                    show: false,
                    dimension: 0,
                    pieces: [{
                        lte: 6,
                        color: 'green'
                    }, {
                        gt: 6,
                        lte: 8,
                        color: 'red'
                    }, {
                        gt: 8,
                        lte: 14,
                        color: 'green'
                    }, {
                        gt: 14,
                        lte: 17,
                        color: 'red'
                    }, {
                        gt: 17,
                        color: 'green'
                    }]
                },
                series: [
                    {
                        name: '用电量',
                        type: 'line',
                        smooth: true,
                        data: [300, 280, 250, 260, 270, 300, 550, 500, 400, 390, 380, 390, 400, 500, 600, 750, 800, 700, 600, 400],
                        markArea: {
                            data: [ [{
                                name: '早高峰',
                                xAxis: '07:30'
                            }, {
                                xAxis: '10:00'
                            }], [{
                                name: '晚高峰',
                                xAxis: '17:30'
                            }, {
                                xAxis: '21:15'
                            }] ]
                        }
                    }
                ]
            };


            myChart.setOption(option);
            myChart2.setOption(option2);
        }
    )




});