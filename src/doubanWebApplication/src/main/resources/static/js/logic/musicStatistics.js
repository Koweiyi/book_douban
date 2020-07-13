layui.use(['jquery','layer','carousel'], function () {
    let $ = layui.jquery,
        layer = layui.layer;

    var carousel = layui.carousel;
    //建造实例
    carousel.render({
        elem: '#lundong'
        ,width: '100%' //设置容器宽度
        ,arrow: 'hover' //始终显示箭头
        ,anim: 'fade' //切换动画方式
        ,height: '300px'
        ,interval: 1500
    });

    // 基于准备好的dom，初始化echarts实例
    let music_mark = echarts.init(document.getElementById('music_mark'));
    let music_site = echarts.init(document.getElementById('music_site'));
    let music_sect = echarts.init(document.getElementById('music_sect'));
    let music_man = echarts.init(document.getElementById('music_man'));

    //第一张表
    $.post(
        "/logic/music/chart1",
        {},
        function (result) {
            let score = [];
            let count = [];

            for (i = 0;i < result.length-2;i++){
                score.push(result[i].score);
                count.push(result[i].count);
            }

            // 指定图表的配置项和数据
            let option = {
                title: {
                    text: '各评分音乐数量统计'
                },
                tooltip: {},
                legend: {
                    data:['评分']
                },
                xAxis: {
                    data: score
                },
                yAxis: {},
                series: [{
                    name: '评分',
                    type: 'bar',
                    data: count
                }]
            };

            // 使用刚指定的配置项和数据显示图表。
            music_mark.setOption(option);

        }
    )

    //第二张表
    $.post(
        "/logic/music/chart2",
        {},
        function (result) {
            let jieguo = [];
            let site = [];

            for (i = 0;i < result.length;i++){

                if (i < 10){
                    jieguo.push({name : result[i].site,value : result[i].count})
                    site.push(result[i].site)
                }
            }

            // 指定图表的配置项和数据
            let option = {
                title: {
                    text: '五星评论来源城市前十'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                legend: {
                    top : 30,
                    orient: 'vertical',
                    left: 10,
                    data: site
                },
                series: [
                    {
                        name: '用户城市',
                        type: 'pie',
                        radius: ['50%', '70%'],
                        selectedOffset : 10,
                        avoidLabelOverlap: true,
                        left: 39,
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: jieguo
                    }
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            music_site.setOption(option);
        }
    )



    //第三张表
    $.post(
        "/logic/music/chart3",
        {},
        function (result) {
            let score = [];
            let count = [];

            for (i = 0;i < result.length;i++){
                score.push(result[i].score);
                count.push(result[i].count);

            }

            // 指定图表的配置项和数据
            let dataAxis = score;
            var data = count;
            var yMax = 500;
            var dataShadow = [];

            for (var i = 0; i < data.length; i++) {
                dataShadow.push(yMax);
            }

            let option = {
                title: {
                    text: '各流派音乐数量统计',
                    subtext: '此统计只针对爬取数据'
                },
                xAxis: {
                    data: dataAxis,
                    axisLabel: {
                        inside: true,
                        textStyle: {
                            color: '#dec411'
                        }
                    },
                    axisTick: {
                        show: false
                    },
                    axisLine: {
                        show: false
                    },
                    z: 10
                },
                yAxis: {
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        textStyle: {
                            color: '#999'
                        }
                    }
                },
                dataZoom: [
                    {
                        type: 'inside'
                    }
                ],
                series: [
                    { // For shadow
                        type: 'bar',
                        itemStyle: {
                            color: 'rgba(0,0,0,0.05)'
                        },
                        barGap: '-100%',
                        barCategoryGap: '40%',
                        data: dataShadow,
                        animation: false
                    },
                    {
                        type: 'bar',
                        itemStyle: {
                            color: new echarts.graphic.LinearGradient(
                                0, 0, 0, 1,
                                [
                                    {offset: 0, color: '#83bff6'},
                                    {offset: 0.5, color: '#188df0'},
                                    {offset: 1, color: '#188df0'}
                                ]
                            )
                        },
                        emphasis: {
                            itemStyle: {
                                color: new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 0, color: '#2378f7'},
                                        {offset: 0.7, color: '#2378f7'},
                                        {offset: 1, color: '#83bff6'}
                                    ]
                                )
                            }
                        },
                        data: data
                    }
                ]
            };

            // Enable data zoom when user click bar.
            var zoomSize = 6;
            music_sect.on('click', function (params) {
                console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
                music_sect.dispatchAction({
                    type: 'dataZoom',
                    startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
                    endValue: dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
                });
            });

            // 使用刚指定的配置项和数据显示图表。
            music_sect.setOption(option);

        }
    )


    //第四张表
    $.post(
        "/logic/music/chart4",
        {},
        function (result) {
            let jieguo = [];
            let man = [];

            for (i = 0;i < result.length;i++){

                if (i < 10){
                    jieguo.push({name : result[i].score,value : result[i].count})
                    man.push(result[i].score)
                }
            }

            let option = {
                title: {
                    text: '高分乐曲数量作家榜',
                    subtext: '此统计只针对爬取数据',
                    left: 0
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                legend: {
                    left: 'center',
                    // top :'bottom',
                    bottom:0,
                    data: man
                },
                toolbox: {
                    show: true,
                    feature: {
                        mark: {show: true},
                        dataView: {show: true, readOnly: false},
                        magicType: {
                            show: true,
                            type: ['pie', 'funnel']
                        },
                        restore: {show: true},
                        saveAsImage: {show: true}
                    }
                },
                series: [
                    // {
                    //     name: '半径模式',
                    //     type: 'pie',
                    //     radius: [20, 110],
                    //     center: ['25%', '50%'],
                    //     roseType: 'radius',
                    //     label: {
                    //         show: false
                    //     },
                    //     emphasis: {
                    //         label: {
                    //             show: true
                    //         }
                    //     },
                    //     data: [
                    //         {value: 10, name: 'rose1'},
                    //         {value: 5, name: 'rose2'},
                    //         {value: 15, name: 'rose3'},
                    //         {value: 25, name: 'rose4'},
                    //         {value: 20, name: 'rose5'},
                    //         {value: 35, name: 'rose6'},
                    //         {value: 30, name: 'rose7'},
                    //         {value: 40, name: 'rose8'}
                    //     ]
                    // },
                    {
                        top:20,
                        left:0,
                        name: '面积模式',
                        type: 'pie',
                        radius: [30, 110],
                        center: ['75%', '50%'],
                        roseType: 'area',
                        data: jieguo

                    }
                ]
            };

            // 使用刚指定的配置项和数据显示图表。
            music_man.setOption(option);

        }
    )







})