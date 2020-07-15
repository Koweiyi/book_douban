//在全局定义验证码
let code;

//产生验证码
$(function(){
    createCode();
    $("#verifyImg").click(function(){
        createCode();
    });
});
function createCode(){
    code = "";
    let codeLength = 4;//验证码的长度
    let checkCode = document.getElementById("verifyImg");
    let random = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z');//随机数
    for(var i = 0; i < codeLength; i++) {//循环操作
        var index = Math.floor(Math.random()*36);//取得随机数的索引（0~35）
        code += random[index];//根据索引取得随机数加到code上
    }
    checkCode.value = code;//把code值赋给验证码
}


layui.use(['jquery','layer'],function () {

    let $ = layui.jquery;
    let layer = layui.layer;

    $("#btnLogin").click(function (event) {
        if($("#uid").val() == ""){
            layer.msg("请填写用户名！");
            return;
        }
        if($("#pwd").val() == ""){
            layer.msg("请填写密码！");
            return;
        }

        if($("#code").val() === ""){
            layer.msg("请填写验证码");
            createCode();//创建新的验证码
            return;
        }

        if($("#code").val().toUpperCase() != code){
            layer.msg("验证码输入错误！@_@");
            $("#code").val("");
            createCode();//创建新的验证码
            return
        }

        $.post(
            '/logic/user/login',
            {
                uid: $("#uid").val(),
                pwd: $("#pwd").val()
            },function (result) {
                if(!result.error){
                    window.location.href = "/html/index.html";
                }
                else{
                    layer.msg("用户名或密码错误！");
                    createCode();
                }
            }
        )

    });

});

//校验验证码
function validate(){
    let uid = document.getElementById("uid").value;
    let pwd = document.getElementById("pwd").value;
    let inputCode = document.getElementById("code").value.toUpperCase(); //取得输入的验证码并转化为大写

    if(uid=="" || pwd==""){
        layui.use(["layer"], function () {
            layer.msg("用户名和密码不能为空！");
        });
        return;
    }

    if(inputCode.length <= 0) { //若输入的验证码长度为0
        layui.use(["layer"], function () {
            layer.msg("请填写验证码");
        });
        // alert("请输入验证码！"); //则弹出请输入验证码
        document.getElementById("code").value = "";//清空文本框
        createCode();
    }
    else if(inputCode != code ) { //若输入的验证码与产生的验证码不一致时
        layui.use(["layer"], function () {
            layer.msg("验证码输入错误！@_@");
        });
        // alert("验证码输入错误！@_@"); //则弹出验证码输入错误
        document.getElementById("code").value = "";//清空文本框
        createCode();
    }else{
        // layui.use(['jquery', 'layer'],function () {
        //
        //     let $ = layui.jquery;
        //     let layer = layui.layer;
        //
        //     $.post(
        //         '/logic/user/login',
        //         {
        //             uid: uid,
        //             pwd: pwd
        //         },
        //         function (result) {
        //             if(result == "redirect:/html/login.html"){
        //                 layer.msg("用户名或密码错误！");
        //             }
        //         }
        //     )
        // });
        postcall("/logic/user/login", {"uid":uid, "pwd":pwd})
    }
}
function postcall( url, params){
    var tempform = document.createElement("form");
    tempform.action = url;
    tempform.method = "post";
    tempform.style.display="none";

    for (var x in params) {
        var opt = document.createElement("input");
        opt.name = x;
        opt.value = params[x];
        tempform.appendChild(opt);
    }

    var opt = document.createElement("input");
    opt.type = "submit";
    tempform.appendChild(opt);
    document.body.appendChild(tempform);
    tempform.submit();
    document.body.removeChild(tempform);
}
