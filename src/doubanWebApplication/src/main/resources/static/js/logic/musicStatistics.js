layui.use(['jquery','layer'], function () {
    let $ = layui.jquery,
        layer = layui.layer;

    // 基于准备好的dom，初始化echarts实例
    let music_mark = echarts.init(document.getElementById('music_mark'));
    let music_site = echarts.init(document.getElementById('music_site'));

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
                    text: '各评分数量统计'
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
                    text: '五星评论来源前十'
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








})