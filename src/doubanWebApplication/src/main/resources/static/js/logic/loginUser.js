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
        }
    )

    $("#login-user-form-yesBtn").click(function (event) {

    });
});