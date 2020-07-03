layui.use(['jquery','form','layer'],function () {
    var $ = layui.jquery,
        form = layui.form,
        layer = layui.layer;

    form.on('submit(login)', function (data) {
        $.post(
            '/logic/user/login',
            {
                'uid': data.field.use,
                'pwd': data.field.pwd
            }
        )
    });

});