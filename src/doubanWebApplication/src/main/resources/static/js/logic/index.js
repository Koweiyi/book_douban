layui.use(['element', 'layer', 'jquery'], function () {
    var element = layui.element;
    var layer = layui.layer;
    var $ = layui.$;

    $(".index-exist").on('click', function () {
        layer.open({
            title: '安全退出',
            content: '您真的要退出当前用户吗？',
            btn:['确认', '取消'],
            btnAlign:'c',
            yes: function (index, layero) {
                window.location.href="/logic/user/logout";
            }
        });
    })

    $('.site-demo-active').on('click', function () {
        var dataid = $(this);
        if ($(".layui-tab-title li[lay-id]").length <= 0) {
            active.tabAdd(dataid.attr("data-url"), dataid.attr("data-id"), dataid.attr("data-title"));
        } else {
            var isData = false;
            $.each($(".layui-tab-title li[lay-id]"), function () {
                if ($(this).attr("lay-id") == dataid.attr("data-id")) {
                    isData = true;
                }
            })
            if (isData == false) {
                active.tabAdd(dataid.attr("data-url"), dataid.attr("data-id"), dataid.attr("data-title"));
            }
        }
        active.tabChange(dataid.attr("data-id"));
    });

    var active = {
        //在这里给active绑定几项事件，后面可通过active调用这些事件
        tabAdd: function (url, id, name) {
            //新增一个Tab项 传入三个参数，分别对应其标题，tab页面的地址，还有一个规定的id，是标签中data-id的属性值
            //关于tabAdd的方法所传入的参数可看layui的开发文档中基础方法部分
            element.tabAdd('demo', {
                title: name,
                content: '<iframe data-frameid="' + id + '" scrolling="auto" frameborder="0" src="' + url + '" style="width:100%;height:100%;"></iframe>',
                id: id //规定好的id
            })
            FrameWH();  //计算ifram层的大小
        },
        tabChange: function (id) {
            //切换到指定Tab项
            element.tabChange('demo', id); //根据传入的id传入到指定的tab项
        },
        tabDelete: function (id) {
            element.tabDelete("demo", id);
        }
    };
    function FrameWH() {
        var h = $(window).height();
        $("iframe").css("height",h+"px");
    }

    let initLoginUser = function () {
        $.post('/logic/user/LoginUser',{},
            function (result) {
                $('#spanNickName').html(result.nickName)
            })
    };

    initLoginUser();

    // element.tabAdd("/html/welcome.html","100","欢迎");
});
