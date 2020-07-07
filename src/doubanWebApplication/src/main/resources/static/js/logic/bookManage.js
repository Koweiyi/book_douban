layui.use(['laydate', 'jquery', 'table', 'form'], function(){

    var laydate = layui.laydate,
        form = layui.form,
        $ = layui.jquery,
        table = layui.table;

    laydate.render({
        elem: '#date'
        ,format: "yyyy"
    });

    table.render({
        elem: '#tblBookResult',
        page: true,
        limit: 30,
        height: 500,
        toolbar : true,
        defaultToolbar:['exports', 'print'],
        cols:[[
            {field: 'id', title: "ID", sort: true, width: 90, align: "center"},
            {field: 'bookName', title: '书名', align: 'center'},
            {field: 'bookAuthor', title: '作者', align: 'center'},
            {field: 'publisher', title: '出版社', align: 'center'},
            {field: 'date', title: '出版日期', align: 'center', sort: true, width: 110},
            {field: 'price', title: '价格', align: 'center', sort: true, width: 80},
            {field: 'page', title: '页数', align: 'center', width: 80, sort: true},
            {field: 'isbn', title: 'ISBN', align: 'center', width: 140, sort: true},
            {field: 'tags', title: '标签', align: 'center'},
            {field: 'rate', title: '评分', align: 'center', width: 80, sort: true},
            {field: 'dbId', title: '操作', align: 'center', width: 145,
                templet: function (rowData) {
                    let btnDetail = '<button class="layui-btn layui-btn-primary layui-btn-xs" lay-event="detail"><i class="layui-icon layui-icon-file"></i>查看</button>',
                        btnEdit = '<button class="layui-btn layui-btn-xs" lay-event="edit"><span><i class="layui-icon layui-icon-edit"></i></span>编辑</button>';
                    return btnDetail + btnEdit;
                }
            }
        ]],
        data:[]
    });



    $('#btnBookSearch').click(function (event) {

        table.reload('tblBookResult',{
            url:'/logic/book/search',
            method:'post',
            where:{
                'bookName': $('#bookName').val(),
                'bookAuthor': $('#bookAuthor').val(),
                'tags': $('#tags').val(),
                'date': $('#date').val(),
                'isbn': $('#isbn').val()
            },
            page: {
                curr: 1
            }
        })

    });
    $('#btnReset').click(function (event) {
        $('#bookName').val("");
        $('#bookAuthor').val("");
        $('#date').val("");
        $('#tags').val("");
        $('#isbn').val("");
    })

});


