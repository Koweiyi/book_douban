layui.use(['jquery','layer'],function () {
    let $ = layui.jquery,
        layer = layui.layer;

    let myChart = echarts.init(document.getElementById('bookCount'));

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

            for (i = 0 ; i < result.length ; i ++){
                score.push(result[i].score);
                count.push(result[i].count);
            }

            // 指定图表的配置项和数据
            let option = {
                title: {
                    text: '图书评分统计'
                },
                tooltip:{},
                legend: {
                    data: ['评分']
                },
                height: 138,
                xAxis: {
                    data: score
                },
                yAxis: {},
                series: [{
                    type: 'bar',
                    data: count
                }]
            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        }
    )
});