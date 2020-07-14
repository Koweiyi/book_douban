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
                            $("#inputPwdTest").val("");
                            layer.closeAll();
                        }
                    }
                )
            }
        })
    });
});