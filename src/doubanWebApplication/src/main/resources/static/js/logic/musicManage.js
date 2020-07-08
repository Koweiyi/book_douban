layui.use(['jquery','form','table','layer'], function () {
    var $ = layui.jquery,
        //form = layui.form,
        table = layui.table;
        //layer = layui.layer;

    table.render({
        elem: '#MusictblResult',
        page: true,
        limit: 6,
        cols: [[
            {field: 'musicId',title:'音乐ID',align:'center',width:'6.5%'},
            {field: 'musicName',title:'音乐名',align:'center',width:'6.5%'},
            {field: 'musicRename',title:'又名',align:'center',width:'5.5%'},
            {field: 'musicMan',title:'表演者',align:'center',width:'6.5%'},
            {field: 'musicSect',title:'流派',align:'center',width:'5.5%'},
            {field: 'musicAlbum',title:'专辑类型',align:'center',width:'8%'},
            {field: 'musicMedia',title:'介质',align:'center',width:'5.5%'},
            {field: 'musicTime',title:'发行时间',align:'center',width:'8%'},
            {field: 'musicMark',title:'评分',align:'center',width:'5.5%'},
            {field: 'musicVote',title:'评价人数',align:'center',width:'8%'},
            {field: 'musicStar5',title:'五星',align:'center',width:'5.5%'},
            {field: 'musicStar4',title:'四星',align:'center',width:'5.5%'},
            {field: 'musicStar3',title:'三星',align:'center',width:'5.5%'},
            {field: 'musicStar2',title:'二星',align:'center',width:'5.5%'},
            {field: 'musicStar1',title:'一星',align:'center',width:'5.5%'},
            {field: 'musicUrl',title:'资源路径',align:'center',width:'8%'},
            /*{field: 'state', title:'用户状态',align:'center',
                templet: function (rowData) {
                    switch (rowData.state) {
                        case 0:


                            return '<font color="yellow">' +
                                '<i class="layui-icon layui-icon-about"></i>' +
                                '<b>未激活</b></font>';
                        case 1:
                            return '<font color="green" ><b>正常</b></font> '
                        case 2:
                            return ' <font color=""”red" ><b>已屏蔽</b></font>';
                    }
                }},*/
            {field: 'caozuo', title: '操作',align:'center',
                templet:function(rowData){
                    /*var btnReset =  '<button class="layui-btn layui-btn-sm layui-btn-warm" lay-event="reset" >' +
                        '<i class="layui-icon layui-icon-password" ></i>密码重置</button>'*/
                    var btnInfo =   '<button class="layui-btn layui-btn-sm layui-btn-normal" lay-event="info">' +
                        '<i class="layui-icon layui-icon-about"></i>编辑详情</button>'
                    var btnDisable ='<button class="layui-btn layui-btn-sm layui-btn-danger" lay-event= "like">' +
                        '<i class="layui-icon layui-icon-close"></i>加入喜欢</button> '
                    return btnInfo + btnDisable;
                }
            }
        ]],
        data:[]
    });

    table.on('tool(tblResult)', function (obj) {

        if('info' === obj.event) {
            alert('歌曲名字:' + obj.data.musicname + "，ID:" + obj.data.id + "请进行编辑");
        }
        if('like' === obj.event) {
            alert(' 歌曲名字:'+ obj.data.musicname +"，ID: "+ obj.data.id +"已加入你的喜欢");
        }
    });

    $('#btnSearch').click( function(event) {
        table. reload('MusictblResult',{
            url:'/logic/music/search2',
            method: 'post',
            where: {
                'musicName' : $('#musicName').val(),
                'musicMan' : $('#musicMan').val(),
                'musicMark' : $('#musicMark').val()
            },
            page: {
                curr:1
            }
        })
    });
});
