layui.use(['jquery', 'form', 'table', 'layer'], function () {

    var $ = layui.jquery,
        form = layui.form,
        table = layui.table
    layer = layui.layer;

    table.render({
        elem: '#tblResult2',
        page: true,
        limit: 6,
        cols: [[
            {field:'id', title:'编号', align:'center'},
            {field:'tag', title: 'tag', align: 'center'},
            {field:'title', title: '电影名', align: 'center'},
            {field:'url', title:'地址', align:'center'},
            {field:'author', title: '导演', align: 'center'},
            {field:'star5', title: '五星', align: 'center'},
            {field:'star4', title:'四星', align:'center'},
            {field:'star3', title: '三星', align: 'center'},
            {field:'star2', title: '二星', align: 'center'},
            {field:'star1', title:'一星', align:'center'},
            {field:'type', title: '类型', align: 'center'},
            {field:'time', title: '发布时间', align: 'center'},
            {field:'short1', title:'短评1', align:'center'},
            {field:'short2', title: '短评2', align: 'center'},
            {field:'short3', title: '短评3', align: 'center'},
        ]],
        data:[]
    });
    /**
     * 页面上的检索按钮的绑定，单击激活检索事件
     * 1）向指定的服务接口（url属性中的链接）以指定方法（POST/GET）发送页面收集的数据（where属性中的JSON数据）
     * 2）并将返回的查询结果填充至指定的LayUI表格控件
     */
    $('#btnSearch2').click(function(event) {

        table.reload('tblResult2', {
            url:'/logic/tv/search2',
            method:'post',
            where: {
                'id' : $('#id').val(),
                'tag' : $('#tag').val(),
                'title' : $('#title').val(),
                'url' : $('#url').val(),
                'author' : $('#author').val(),
                'star5' : $('#star5').val(),
                'star4' : $('#star4').val(),
                'star3' : $('#star3').val(),
                'star2' : $('#star2').val(),
                'star1' : $('#star1').val(),
                'type' : $('#type').val(),
                'time' : $('#time').val(),
                'short1' : $('#short1').val(),
                'short2' : $('#short2').val(),
                'short3' : $('#short3').val(),
            },
            page: {
                curr: 1
            }
        })

    });

});