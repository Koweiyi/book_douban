layui.use(['jquery','form','table','layer'], function () {
    var $ = layui.jquery,
        form = layui.form,
        table = layui.table,
        layer = layui.layer;

    table.render({
        elem: '#MovietblResult',
        page: true,
        limit: 6,
        cols: [[
            {field: 'dbid',title:'dbid',align:'center',width:'6%'},
            {field: 'other_title',title:'电影又名',align:'center',width:'8%'},
            {field: 'direct',title:'导演',align:'center',width:'5.5%'},
            {field: 'country',title:'国家',align:'center',width:'5.5%'},
            {field: 'movie_time',title:'电影时长',align:'center',width:'8%'},
            {field: 'movie_type',title:'电影类型',align:'center',width:'8%'},
            {field: 'vote_num',title:'评分人数',align:'center',width:'8%'},
            {field: 'five_star',title:'五星',align:'center',width:'5.5%'},
            {field: 'four_star',title:'四星',align:'center',width:'5.5%'},
            {field: 'three_star',title:'三星',align:'center',width:'5.5%'},
            {field: 'two_star',title:'二星',align:'center',width:'5.5%'},
            {field: 'one_star',title:'一星',align:'center',width:'5.5%'}
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
                'dbid' : $('#dbid').val(),
                //'five_star' :$('#five_star').val()
            },
            page: {
                curr:1
            }
        })
    });
});