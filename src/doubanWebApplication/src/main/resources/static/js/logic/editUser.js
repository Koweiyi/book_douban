layui.use(['layer','form','jquery'], function () {
    var layer = layui.layer,
        form = layui.form,
        $ = layui.jquery;

    form.on('submit(editAndCommit)', function (data) {
        $.post(
            '/logic/user/edit',
            {
                'id' : data.field.id,
                'oldPwd' : data.field.oldPwd,
                'newUid' : data.field.newUid,
                'newPwd' : data.field.newPwd,
                'newNickName' : data.field.newNickName
            },
            function (returnData) {
                if(returnData!=null){
                    layer.alert("用户信息编辑成功！");
                }
            }
        )
    });
});