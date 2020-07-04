layui.use(['jquery', 'form', 'table'], function () {

    var $ = layui.jquery,
        form = layui.form,
        table = layui.table;

    table.render({
       elem: '#tblResult',
       cols: [[
           {field: 'uid', title: '用户名', align: 'center'},
           {field: 'nickName', title: '昵称', align: 'center'},
           {field: 'state', title: '用户状态', align: 'center'}
       ]],
        data: []
    });

    $('#btnSearch').click(function (event) {

        table.reload('tblResult', {
            url:'/logic/user/search',
            method:'post',
            where:{
                'uid' : $('#uid').val(),
                'nickName' : $('#nickName').val(),
                'state' : $('#selState').val()
            }
        })
    });
});