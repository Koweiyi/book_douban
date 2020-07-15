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
        let pwd = $("#pwd").val();
        if(pwd == ""){
            layer.msg("请填写密码！");
            return;
        }else if(pwd.length < 6){
            layer.msg("密码长度不能小于六位！");
            return;
        }else{
            let regPassword =  {
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

        if($("#rePwd").val() == ""){
            layer.msg("请填写确认密码！");
            return;
        }

        if($("#code").val() == ""){
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
                    layer.msg("恭喜，您已经成功注册！");
                    // layer.open({
                    //     title:"恭喜",
                    //     content:"您已经成功注册！",
                    //     yes:function () {
                    //         // window.location.href="/html/login.html";
                    //     }
                    // });
                }else{
                    layer.msg("服务器错误，注册失败！");
                }
            }

        )
    });
});