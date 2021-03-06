layui.use(['jquery', 'form', 'table', 'layer', 'laypage', 'element'], function () {

    var $ = layui.jquery,
        form = layui.form,
        table = layui.table,
        layer = layui.layer,
        laypage = layer.laypage,
        element = layer.element;

    table.render({
        elem: '#tblResult',
        height: 490,
        page: true,
        limit: 20,
        toolbar: true,
        defaultToolbar:['exports', 'print'],
        cols: [[
            {type:'checkbox', fixed: 'left'},
            {field: 'uid', title: '用户名', align: 'center'},
            {field: 'nickName', title: '昵称', align: 'center', edit: 'text'},
            {field: 'state', title: '用户状态', align: 'center',
                templet: function (rowData) {
                    switch (rowData.state) {
                        case 0:
                            return "<span style='color: yellowgreen'><i class='layui-icon layui-icon-tips'></i><b>未激活用户</b></span>";
                        case 1:
                            return "<span style='color: green'><i class='layui-icon layui-icon-ok-circle'></i><b>正常用户</b></span>"
                        case 2:
                            return "<span style='color: red'><i class='layui-icon layui-icon-close-fill'></i><b>屏蔽用户</b></span>"
                        case 3:
                            return "<span style='color: darkblue'><i class='layui-icon layui-icon-auz'></i><b>管理员</b></span>"
                    }
                }
            },
            {field: 'id', title: "操作", align: 'center',
                templet: function (rowData) {
                    let btnPwdReSet='<button class="layui-btn layui-btn-danger layui-btn-xs" lay-event="reSetPwd"><span><i class="layui-icon layui-icon-refresh"></i></span>密码重置</button>';
                    let btnStateManage = '<button class="layui-btn layui-btn-xs" lay-event="stateManage"><span><i class="layui-icon layui-icon-edit"></i></span>状态管理</button>'

                    return btnPwdReSet + btnStateManage;
                }
            }
        ]],
        data: [],
        page: true,

    });

    table.on('tool(tblResult)', function (object) {
        if ("reSetPwd" === object.event) {
            let index = layer.open({
                title:"警告",
                offset:170,
                width:200,
                content:"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;您将重置当前用户：" + object.data.uid + "的密码。</br>" +
                    "<span style='color: #ff0000;'><i class='layui-icon layui-icon-tips'></i></span>该操作不可逆，请慎重考虑!",
                btn:["确认","取消"],
                btnAlign:"c",
                yes: function () {
                    $.post(
                        '/logic/user/resetPwd',
                        {
                            'id': object.data.id
                        },
                        function (data) {
                            layer.msg(data.content);
                            layer.close(index);
                        }

                    )
                }
            });
        }
        else if("stateManage" === object.event){

                $.post('/logic/user/' + object.data.id,{},
                    function (result) {
                        $('#spanEditUid').attr("placeholder",result.uid);
                        // $('#selectState').options[parseInt(result.state)].selected = true;

                        layer.open({
                            type:1,
                            title:"用户权限管理",
                            content: $('#divUserInfo'),
                            area: ['40%', '45%'],
                            btn: ["设置", "取消"],
                            offset:70,
                            btnAlign: "c",
                            yes: function (index, lo) {
                                $.post('/logic/user/setState',
                                    {
                                        'id': result.id,
                                        'state': $("#selectState").val()
                                    },
                                    function (result) {
                                        if(!result.error){
                                            layer.msg("用户权限设置成功！");
                                            table.reload('tblResult', {
                                                url:'/logic/user/search',
                                                method:'post',
                                                where:{
                                                    'uid' : $('#uid').val(),
                                                    'nickName' : $('#nickName').val(),
                                                    'state' : $('#selState').val()
                                                }
                                            })
                                            layer.close(index);
                                        }else{
                                            layer.msg("用户权限设置失败！")
                                        }
                                    }
                                );
                            },
                            btn2: function () {
                                layer.closeAll();
                            }
                        });
                    }
                );
        }
    });


    $('#btnSearch').click(function (event) {

        table.reload('tblResult', {
            url:'/logic/user/search',
            method:'post',
            where:{
                'uid' : $('#uid').val(),
                'nickName' : $('#nickName').val(),
                'state' : $('#selState').val()
            },
            page :{
                curr:1
            }
        })
    });

    $('#btnRefresh').click(function (event) {
        $('#uid').val("");
        $('#nickName').val("");

        set_select_checked("selState", "-1");
    })
    function set_select_checked(selectId, checkValue){
        var select = document.getElementById("selState");

        for (var i = 0; i < select.options.length; i++){
            if (select.options[i].value == checkValue){
                select.options[i].selected = true;
                break;
            }
        }
    }
});