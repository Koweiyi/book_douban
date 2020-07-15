let user;
layui.use(['jquery', 'layer', 'form'],function () {

    let $ = layui.jquery,
        layer = layui.layer,
        form = layui.form;

    $.get(
        '/logic/user/LoginUser',
        {},
        function (result) {
            $("#login-user-uid").attr("placeholder",result.uid);
            $("#login-user-old-nickName").attr("placeholder",result.nickName);
            user = result;
        }
    )

    $("#login-user-form-yesBtn").click(function (event) {

        if($("#login-user-pwd").val()=="" && $("#login-user-nickName").val() == ""){
            layer.msg("您尚未做出任何用户修订！");
            return;
        }

        let pwd = $("#login-user-pwd").val();

        if(pwd.length <= 5){
            layer.msg("密码长度不能小于六位！");
            return;
        }else{
            let regPassword = {
                regStr:/^[\w@#*]{6,16}$/,
                numStr:/^[0-9]*$/,
                letterStr:/^[a-zA-Z]*$/,
            };
            if(regPassword.numStr.test(pwd)){
                layer.msg("密码不能为纯数字");
                return;
            }
            if(regPassword.letterStr.test(pwd)){
                layer.msg("密码不能为纯字母");
                return;
            }
            if(!regPassword.regStr.test($("#pwd").val())){
                layer.msg("密码不能包含@，#，*之外的特殊字符！");
                return;
            }
        }

        let index = layer.open({
            type:1,
            title:"用户验证",
            area:["30%", "24%"],
            content:$("#divUserTest"),
            btn:["确定"],
            btnAlign:"c",
            yes: function () {
                $.post(
                    '/logic/user/userTest',
                    {
                        uid: user.uid,
                        pwd: $("#inputPwdTest").val()
                    },
                    function (result) {
                        if(!result.error){
                            $.post(
                                '/logic/user/updateUser',
                                {
                                    uid: user.uid,
                                    nickName: $("#login-user-nickName").val(),
                                    pwd: $("#login-user-pwd").val()
                                },
                                function (result) {
                                    layer.close(index);
                                    if(!result.error){
                                        layer.open({
                                            title:"提示",
                                            content:"用户信息修改成功，将为您重新登录！",
                                            btn:"确定",
                                            yes: function () {
                                                $.post(
                                                    '/logic/user/login',
                                                    {
                                                        uid: user.uid,
                                                        pwd: $("#login-user-pwd").val()
                                                    },
                                                    function (result) {
                                                        parent.location.reload();
                                                    }
                                                )
                                            }
                                        })
                                    }
                                }
                            )
                        }
                        else{
                            layer.msg("密码输入错误");
                        }
                    }
                )
                $("#inputPwdTest").val("");
                layer.close(index);
            }
        })
    });
});