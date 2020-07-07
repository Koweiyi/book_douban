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
            // layer.open({
            //     type: 1,
            //     title: "编辑",
            //     area: ['50%', '50%'],
            //     btn: false,
            //     height: 400,
            //     content: "<!DOCTYPE html>\n" +
            //         "<html lang=\"en\">\n" +
            //         "<head>\n" +
            //         "    <meta charset=\"UTF-8\">\n" +
            //         "    <title>Title</title>\n" +
            //         "    <link rel=\"stylesheet\" href=\"/css/main.css\", media=\"all\">\n" +
            //         "    <link rel=\"stylesheet\" href=\"/js/layui/css/layui.css\">\n" +
            //         "</head>\n" +
            //         "<body>\n" +
            //         "\n" +
            //         "<form class=\"layui-form layui-form-pane\" id=\"edit-user-form\">\n" +
            //         "    <ul>\n" +
            //         "        <li class=\"layui-form-item\">\n" +
            //         "            <label class=\"layui-form-label\">id：</label>\n" +
            //         "            <div class=\"layui-input-block\">\n" +
            //         "                <input type=\"text\" readonly=\"readonly\" class=\"layui-input\" id=\"id\" placeholder=" + object.data.id + " value=" + object.data.id + " name=\"id\">\n" +
            //         "            </div>\n" +
            //         "        </li>\n" +
            //         "        <li class=\"layui-form-item\">\n" +
            //         "            <label class=\"layui-form-label\">旧密码：</label>\n" +
            //         "            <div class=\"layui-input-block\">\n" +
            //         "                <input type=\"password\" class=\"layui-input\" id=\"oldPwd\" placeholder=\"*********\" required lay-verify=\"required\" name=\"oldPwd\">\n" +
            //         "            </div>\n" +
            //         "        </li>\n" +
            //         "        <li class=\"layui-form-item\">\n" +
            //         "            <label class=\"layui-form-label\">用户名：</label>\n" +
            //         "            <div class=\"layui-input-block\">\n" +
            //         "                <input type=\"text\" class=\"layui-input\" id=\"newUid\"  name=\"newUid\">\n" +
            //         "            </div>\n" +
            //         "        </li>\n" +
            //         "        <li class=\"layui-form-item\">\n" +
            //         "            <label class=\"layui-form-label\">昵称：</label>\n" +
            //         "            <div class=\"layui-input-block\">\n" +
            //         "                <input type=\"text\" class=\"layui-input\" id=\"newNickName\" required  name=\"newNickName\">\n" +
            //         "            </div>\n" +
            //         "        </li>\n" +
            //         "        <li class=\"layui-form-item\">\n" +
            //         "            <label class=\"layui-form-label\">密码：</label>\n" +
            //         "            <div class=\"layui-input-block\">\n" +
            //         "                <input type=\"password\" class=\"layui-input\" id=\"newPwd\" placeholder=\"输入新密码\" name=\"newPwd\">\n" +
            //         "            </div>\n" +
            //         "        </li>\n" +
            //         "        <li class=\"layui-form-item\">\n" +
            //         "            <button id=\"btnEdit\" class=\"layui-btn\" lay-submit lay-filter=\"editAndCommit\">编辑用户</button>\n" +
            //         "        </li>\n" +
            //         "    </ul>\n" +
            //         "</form>\n" +
            //         "\n" +
            //         "<script type=\"text/javascript\" src=\"/js/layui/layui.all.js\"></script>\n" +
            //         "<script type=\"text/javascript\" src=\"/js/logic/editUser.js\"></script>\n" +
            //         "</body>\n" +
            //         "</html>\n",
            // });
            let index = layer.open({
                title:"警告",
                width:200,
                content:"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;您将重置当前用户：" + object.data.uid + "的密码。</br>" +
                    "<span style='color: #ff0000;'><i class='layui-icon layui-icon-tips'></i>该操作不可逆，请慎重考虑!</span> ",
                btn:["确认","取消"],
                btnAlign:"c",
                yes: function () {
                    $.post(
                        '/logic/user/resetPwd',
                        {
                            'id': object.data.id
                        },
                        function (data) {
                            layer.alert(data.content);
                            layer.close(index);
                        }

                    )
                }
            });
        }

        else if("stateManage" === object.event){

        }
    })


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