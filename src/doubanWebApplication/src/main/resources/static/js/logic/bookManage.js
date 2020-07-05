layui.use(['laydate', 'jquery', 'table', 'form'], function(){

    var laydate = layui.laydate,
        form = layui.form,
        $ = layui.jquery,
        table = layui.table;

    laydate.render({
        elem: '#date'
        ,format: "yyyy-M"
    });

    table.render({
        elem: '#tblBookResult',
        page: true,
        limit: 30,
        height: 500,
        theme : "#1e9fff",
        cols:[[
            {field: 'id', title: "ID", sort: true, width: 100, align: "center"},
            {field: 'bookName', title: '书名', align: 'center'},
            {field: 'bookAuthor', title: '作者', align: 'center'},
            {field: 'publisher', title: '出版社', align: 'center'},
            {field: 'date', title: '出版日期', align: 'center', sort: true, width: 120},
            {field: 'price', title: '价格', align: 'center', sort: true, width: 120},
            {field: 'page', title: '页数', align: 'center', width: 100, sort: true},
            {field: 'isbn', title: 'ISBN', align: 'center', width: 140, sort: true},
            {field: 'tags', title: '豆瓣标签', align: 'center'},
            {field: 'rate', title: '豆瓣评分', align: 'center', width: 100, sort: true}
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

});


