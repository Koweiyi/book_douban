layui.use(['jquery','form','table','layer'], function () {
    var $ = layui.jquery,
        //form = layui.form,
        table = layui.table;
        //layer = layui.layer;

    table.render({
        elem: '#tblResult',
        page: true,
        limit: 6,
        cols: [[
            {field: 'm_name',title:'音乐名',align:'center'},
            {field: 'm_man',title:'作者',align:'center'},
            {field: 'm_mark',title:'评分',align:'center'},
            /*{field: 'state', title:'用户状态',align:'center',
                templet: function (rowData) {
                    switch (rowData.state) {
                        case 0:


                            return '<font color="yellow">' +
                                '<i class="layui-icon layui-icon-about"></i>' +
                                '<b>未激活</b></font>';
                        case 1:
                            return '<font color="green" ><b>正常</b></font> '
                        case 2:
                            return ' <font color=""”red" ><b>已屏蔽</b></font>';
                    }
                }},*/
            {field: 'id', title: '操作',align:'center',
                templet:function(rowData){
                    /*var btnReset =  '<button class="layui-btn layui-btn-sm layui-btn-warm" lay-event="reset" >' +
                        '<i class="layui-icon layui-icon-password" ></i>密码重置</button>'*/
                    var btnInfo =   '<button class="layui-btn layui-btn-sm layui-btn-normal" lay-event="info">' +
                        '<i class="layui-icon layui-icon-about"></i>编辑详情</button>'
                    var btnDisable ='<button class="layui-btn layui-btn-sm layui-btn-danger" lay-event= "like">' +
                        '<i class="layui-icon layui-icon-close"></i>加入喜欢</button> '
                    return btnInfo + btnDisable;
                }
            }
        ]],
        data:[]
    });

    table.on('tool(tblResult)', function (obj) {

        /*if('reset' === obj.event){
            // alert('密码重置一uid: ’+ obj.data.uid +”，ID: ”+ obj.data.id);
            let index = layer .open({
                title:'警告',
                content:'您将重置当前用户: ' + obj.data.uid + ' 的密码，请确认! </br>注意，该操作不可逆',
                btn: ['确认','取消'],
                btnAlign:'C',
                yes: function () {
                    $.post(
                        '/1ogic/user/pwdreset',
                        {
                            'id': obj.data.id
                        },
                        function (data) {
                            let msg = '服务器错误,请联系管理员';
                            if (!data.error) {
                                msg = '您已经成功重置了该用户的密码';
                            }
                            layer.alert(msg);
                            layer.close(index);
                        }
                    )
                },
                btn2: function () {
                    layer.closeAll();
                }
            });
        }*/
        if('info' === obj.event) {
            alert('歌曲名字:' + obj.data.m_name + "，ID:" + obj.data.id + "请进行编辑");
        }
        if('like' === obj.event) {
            alert(' 歌曲名字:'+ obj.data.m_name +"，ID: "+ obj.data.id +"已加入你的喜欢");
        }
    });

    $('#btnSearch').click( function(event) {
        table. reload('tblResult',{
            url:'/logic/music/search2',
            method: 'post',
            where: {
                'm_name' : $('#m_name').val(),
                'm_mam' : $('#m_man').val(),
                'm_mark' : $('#m_mark').val()
            },
            page: {
                curr:1
            }
        })
    });
});
