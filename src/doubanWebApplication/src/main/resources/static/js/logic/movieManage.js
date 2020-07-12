layui.use(['jquery','form','table','layer'], function () {
    var $ = layui.jquery,
        form = layui.form,
        table = layui.table,
        layer = layui.layer;

    table.render({
        elem: '#MovietblResult',
        page: true,
        limit: 10,
        height: 500,
        cols: [[
            {field: 'dbid',title:'dbid',align:'center',width:'7.5%'},
            {field: 'otherTitle',title:'电影又名',align:'center',width:'15%'},
            {field: 'direct',title:'导演',align:'center',width:'12%'},
            {field: 'country',title:'国家',align:'center',width:'8%'},
            {field: 'movieTime',title:'电影时长',align:'center',width:'12%'},
            {field: 'movieType',title:'电影类型',align:'center',width:'12%'},
            {field: 'voteNum',title:'评分人数',align:'center',width:'7%'},
            {field: 'fiveStar',title:'五星',align:'center',width:'5.5%'},
            {field: 'fourStar',title:'四星',align:'center',width:'5.5%'},
            {field: 'threeStar',title:'三星',align:'center',width:'5.5%'},
            {field: 'twoStar',title:'二星',align:'center',width:'5.5%'},
            {field: 'oneStar',title:'一星',align:'center',width:'5.5%'}
        ]],
        data:[]
    });

    $('#btnSearch').click(function (event) {
        table.reload('MovietblResult',{
            url: '/logic/movie/search_movie',
            method: 'post',
            where:{
                'direct' : $('#direct').val(),
                'country' : $('#country').val(),
                'dbid' : $('#dbid').val()
                //'five_star' :$('#five_star').val()
            },
            page: {
                curr:1
            }
        })
    });
});