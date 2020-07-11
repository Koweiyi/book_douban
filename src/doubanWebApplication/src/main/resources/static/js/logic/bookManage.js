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
                    let btnDetail = '<button class="layui-btn layui-btn-primary layui-btn-xs" lay-event="detail"><i class="layui-icon layui-icon-file"></i>详情</button>',
                        btnEdit = '<button class="layui-btn layui-btn-xs" lay-event="edit"><span><i class="layui-icon layui-icon-edit"></i></span>编辑</button>';
                    return btnDetail + btnEdit;
                }
            }
        ]],
        data:[]
    });

    table.on('tool(tblBookResult)', function (object) {
        if("detail" === object.event){
            $.post(
                '/logic/book/' + object.data.id,
                {},
                function (result) {

                    $('#imgBookInfo').attr("src","/imgs/" + result.book.picSha1);
                    $('#spamBookName').html("书名：" + result.book.bookName);
                    if(result.book.bookAuthor!=null)
                        $('#spamBookAuthor').html(result.book.bookAuthor);
                    else
                        $('#spamBookAuthor').attr("display","none")

                    if(result.book.publisher!=null)
                        $('#spamBookPublisher').html(result.book.publisher);
                    else
                        $('#spamBookPublisher').attr("display","none")

                    if(result.book.date!=null)
                        $('#spamBookDate').html(result.book.date);
                    else
                        $('#spamBookDate').attr("display","none")

                    if(result.book.page!=null)
                        $('#spamBookPage').html(result.book.page);
                    else
                        $('#spamBookPage').attr("display","none")

                    if(result.book.price!=null)
                        $('#spamBookPrice').html(result.book.price);
                    else
                        $('#spamBookPrice').attr("display","none")

                    if(result.book.isbn!=null)
                        $('#spamBookIsbn').html(result.book.isbn);
                    else
                        $('#spamBookIsbn').attr("display","none")

                    if(result.book.tags!=null)
                        $('#spamBookTag').html(result.book.tags);
                    else
                        $('#spamBookTag').attr("display","none")

                    $('#spamBookId').html(result.book.id);
                    if(result.book.rate != null){
                        $('#spamBookRate').html(result.book.rate);
                        $('#spamBookRatePl').html(result.book.ratePl);
                        $('#spamBookFourStar').html(result.book.fourStar);
                        $('#spamBookFiveStar').html(result.book.fiveStar);
                        $('#spamBookThreeStar').html(result.book.threeStar);
                        $('#spamBookTwoStar').html(result.book.twoStar);
                        $('#spamBookOneStar').html(result.book.oneStar);
                    }

                    $('#spanBookIntro').html(result.book.intro);
                    $('#spanComment1').html(result.comments[0].content);
                    let index = layer.open({
                        type:1,
                        title:"图书详情信息",
                        offset:'30px',
                        content:$("#divBookInfo"),
                        area:['40%','65%'],
                    });

                }

            )
        }else if("edit" === object.event){
            layer.msg("编辑按钮被点击了");
        }
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



