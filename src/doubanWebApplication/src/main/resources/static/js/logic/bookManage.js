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
        elem: '#tblResult',
        page: true,
        limit: 6,
        cols:[[
           {field: 'bookName', title: '书名', align: 'center'},
           {field: 'bookAuthor', title: '作者', align: 'center'},
           {field: 'publisher', title: '出版社', align: 'center'},
           {field: 'date', title: '出版日期', align: 'center'},
           {field: 'price', title: '价格', align: 'center'},
           {field: 'page', title: '页数', align: 'center'},
           {field: 'isbn', title: 'ISBN', align: 'center'},
           {field: 'rate', title: '豆瓣评分', align: 'center'}
        ]],
        data:[]
    });

    $('#btnBookSearch').click(function (event) {

        table.reload('tblResult',{
            uri:'logic/book/search',
            method:'post',
            where:{
                'bookName': $('#bookName').val(),
                'bookAuthor': $('#bookAuthor').val(),
                'tags': $('#bookType').val(),
                'date': $('#date').val(),
                'isbn': $('#isbn').val()
            },
            page: {
                curr: 1
            }
        })

    });

});


