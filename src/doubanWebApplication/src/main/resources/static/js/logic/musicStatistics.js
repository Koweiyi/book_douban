layui.use(['jquery','layer'], function () {
    let $ = layui.jquery,
        layer = layui.layer;

    // 基于准备好的dom，初始化echarts实例
    let myChart = echarts.init(document.getElementById('music_mark'));

    $.post(
        "/logic/music/chart1",
        {},
        function (result) {
            let score = [];
            let count = [];

            for (i = 0;i < result.length;i++){
                score.push(result[i].score);
                count.push(result[i].count);
            }

            // 指定图表的配置项和数据
            let option = {
                title: {
                    text: '评分统计'
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
            myChart.setOption(option);

        }
    )








})