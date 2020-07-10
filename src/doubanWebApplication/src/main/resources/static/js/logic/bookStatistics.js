layui.use(['jquery','layer'],function () {
    let $ = layui.jquery,
        layer = layui.layer;

    let myChart = echarts.init(document.getElementById('bookCount'));
    let pageChart = echarts.init(document.getElementById('priceCount'));
    let tagChart = echarts.init(document.getElementById('tagCount'));
    let publisherChart = echarts.init(document.getElementById('publisherCount'));

    $.get(
        '/logic/book/count/allBookCount',
        {},
        function (result) {
            $('#spanBookCount').html(result.count);
        }
    )

    $.get(
        '/logic/book/count/authorCount',
        {},
        function (result) {
            $('#spanAuthorCount').html(result.count);
        }
    )

    $.get(
        '/logic/book/count/publisherCount',
        {},
        function (result) {
            $("#spanPublisherCount").html(result.count);
        }
    )

    $.get(
        '/logic/book/count/scoreCount',
        {},
        function (result) {
            // console.log(result);

            let score = [],
                count = [];

            for (i = 0 ; i < 40 ; i ++){
                score.push(result[i].score);
                count.push(result[i].count);
            }

            // 指定图表的配置项和数据
            let option = {
                title: {
                    subtext: '图书评分统计',
                },
                tooltip:{},
                legend: {
                    data: ['评分']
                },
                height: 139,
                xAxis: {
                    type: 'category',
                    data: score
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    type: 'line',
                    data: count,
                    smooth: true,
                    areaStyle: {
                        color:"#bd9af4",
                        opacity:0.5
                    },
                    itemStyle:{
                      normal:{
                          color:'#bd9af4',
                          lineStyle:{
                              color:"#bd9af4"
                          }
                      }
                    }
                }]
            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        }
    )

    $.get(
        '/logic/book/count/priceCount',
        {},
        function (result) {

            console.log(result);

            let price = [],
                count = [];

            for (i = 0 ; i < 10 ; i ++){
                price.push((i * 10).toString() + "~" + (i * 10 + 10).toString());
                let sum = 0;
                for(j = 0 ; j < 10 ; j ++){
                    sum += result[i * 10 + j].v;
                }
                count.push(sum);
            }

            let option = {
                height: 139,
                title: {
                    subtext: '图书价格统计',
                },
                xAxis: {
                    data: price
                },
                yAxis: {},
                series: [{
                    data: count,
                    type: 'bar',
                    itemStyle: {
                        normal: {
                            color: function (params) {
                                let colorList = ['#c23513', "#2f4554", "#61a0a8", "#d48265", "#91c7ae", "#749f83", "#ca8622","#e542d8", "#314f45", "#ff7723"];
                                return colorList[params.dataIndex];
                            }
                        }
                    }
                }]
            };
            pageChart.setOption(option);
        }
    )

    $.get(
        '/logic/book/count/tagCount',
        {},
        function (result) {

            let name = [];
            for(i = 0 ; i < 6 ; i ++){
                name.push(result[i].name);
            }

            let option = {
                height: 240,
                title: {
                    subtext: "热门图书标签比例",
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: name
                },
                series: [
                    {
                        name: '图书标签',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '60%'],
                        data: result,
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };
            tagChart.setOption(option);
        }
    )

    $.get(
        '/logic/book/count/publisherClassify',
        {},
        function (result) {
            let option = {
                backgroundColor: '#FFFFFF',
                height:235,
                title: {
                    subtext: '主要图书出版社比例',
                },

                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                visualMap: {
                    show: false,
                    min: 200,
                    max: 450,
                    inRange: {
                        colorLightness: [0, 1]
                    }
                },
                series: [
                    {
                        name: '图书出版社',
                        type: 'pie',
                        radius: '70%',
                        center: ['50%', '60%'],
                        data: result.sort(function (a, b) { return a.value - b.value; }),
                        roseType: 'radius',
                        label: {
                            color: '#d48265'
                        },
                        labelLine: {
                            lineStyle: {
                                color: 'purple'
                            },
                            length: 3,
                            smooth: 0.5,
                        },
                        animationType: 'scale',
                        animationEasing: 'elasticOut',
                        animationDelay: function (idx) {
                            return Math.random() * 200;
                        },
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };
            publisherChart.setOption(option);
        }
    )



});