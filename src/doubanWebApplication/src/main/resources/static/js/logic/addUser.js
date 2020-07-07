layui.use(['layer','form','jquery'], function () {
    var layer = layui.layer,
        form = layui.form,
        $ = layui.jquery;

    // form.on('submit(btnRegister)', function (data) {
    //     $.post(
    //         '/logic/user/add',
    //         {
    //             'rePwd' : data.field.rePwd,
    //             'uid' : data.field.uid,
    //             'pwd' : data.field.pwd,
    //             'nickName' :data.field.nickName
    //         },
    //         function (returnData) {
    //             if(returnData != null){
    //                 layer.alert("恭喜您！用户注册成功", window.location.href="/html/login.html");
    //             }
    //             else{
    //                 layer.alert("用户注册失败，请重新注册！", window.location.href="/html/register.html");
    //             }
    //         }
    //     )
    // });

    // $("#btnRegister").click(function (event) {
    //     $.post(
    //         "/logic/user/add",
    //         {
    //             'rePwd' : $('#rePwd').val(),
    //             'uid' : $('#uid').val(),
    //             'pwd' : $('#pwd').val(),
    //             'nickName' :$('#nickName').val()
    //         },
    //         function (returnData) {
    //             if(returnData != null){
    //                 layer.alert("用户注册成功！");
    //                 window.location.href="/html/login.html";
    //             }else{
    //                 layer.alert("用户注册失败！");
    //                 window.location.href="/html/register.html";
    //             }
    //
    //         }
    //
    //     )
    // });
});