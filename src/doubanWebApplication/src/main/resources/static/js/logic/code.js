var code ; //在全局定义验证码
//产生验证码
$(function(){
    createCode();
    $("#verifyImg").click(function(){
        createCode();
    });
});
function createCode(){
    code = "";
    var codeLength = 4;//验证码的长度
    var checkCode = document.getElementById("verifyImg");
    var random = new Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z');//随机数
    for(var i = 0; i < codeLength; i++) {//循环操作
        var index = Math.floor(Math.random()*36);//取得随机数的索引（0~35）
        code += random[index];//根据索引取得随机数加到code上
    }
    checkCode.value = code;//把code值赋给验证码
}

//校验验证码
function validate(){
    let uid = document.getElementById("uid").value;
    let pwd = document.getElementById("pwd").value;
    let inputCode = document.getElementById("code").value.toUpperCase(); //取得输入的验证码并转化为大写

    if(uid=="" || pwd==""){
        layui.use(["layer"], function () {
            alert("用户名和密码不能为空！");
        });
        return;
    }

    if(inputCode.length <= 0) { //若输入的验证码长度为0
        alert("请输入验证码！"); //则弹出请输入验证码
        document.getElementById("code").value = "";//清空文本框
        createCode();
    }
    else if(inputCode != code ) { //若输入的验证码与产生的验证码不一致时
        alert("验证码输入错误！@_@"); //则弹出验证码输入错误
        document.getElementById("code").value = "";//清空文本框
        createCode();
    }else{
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
