layui.use(['jquery','layer'],function () {

    let $ = layui.$,
        layer = layui.layer;

    let myChart = echarts.int(document.getElementById('tvcount'))

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
                score.push(result[i].score);
                count.push(result[i].count);

                if(i <= 10)
                    pieCount.push({'value':result[i].count,'name':result[i].score});
            }
            let option = {
                xAxis: {
                    type: 'category',
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: count,
                    type: 'line'
                }]
            };
        }

    )




})