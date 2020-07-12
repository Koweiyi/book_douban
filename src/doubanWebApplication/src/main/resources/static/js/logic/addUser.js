layui.use(['layer','form','jquery'], function () {
    var layer = layui.layer,
        form = layui.form,
        $ = layui.jquery;

    $("#btnRegister").click(function (event) {

        if($("#uid").val() == ""){
            layer.msg("请填写用户名！");
            return;
        }
        if($("#nickName").val() == ""){
            layer.msg("请填写昵称！");
            return;
        }
        if($("#pwd").val() == ""){
            layer.msg("请填写密码！");
            return;
        }
        if($("#rePwd").val() == ""){
            layer.msg("请填写确认密码！");
            return;
        }


        $.post(
            "/logic/user/indexUser",
            {
                "uid":$("#uid").val(),
            },
            function (result) {
                if(result.error){
                    layer.msg("当前用户名已经被注册！");
                    return;
                }
            }
        )

        if($("#rePwd").val()!=$("#pwd").val()){
            layer.msg("两次密码输入不一致，请重新输入！");
            $("#rePwd").val("");
            $("#pwd").val("");
            return;
        }

        $.post(
            "/logic/user/add",
            {
                'rePwd' : $('#rePwd').val(),
                'uid' : $('#uid').val(),
                'pwd' : $('#pwd').val(),
                'nickName' :$('#nickName').val()
            },
            function (returnData) {
                if(returnData != null){
                    layer.open({
                        title:"恭喜",
                        content:"您已经成功注册！",
                        yes:function () {
                            window.location.href="/html/login.html";
                        }
                    });
                }else{
                    layer.msg("服务器错误，注册失败！");
                }
            }

        )
    });
});