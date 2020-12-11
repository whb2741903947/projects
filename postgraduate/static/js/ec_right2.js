var ec_right2 = echarts.init(document.getElementById('right2'));

var data =[{'name': '211', 'value': '4'}, {'name': '一次', 'value': '2'}, {'name': '加油', 'value': '4'}, {'name': '学习', 'value': '2'}, {'name': '每天', 'value': '3'}]

var ec_right2_option = {
    title : {
        text: '考生评论词云图',
        textStyle:{
            color:"white",
        },
        left:"center"
    },
    tooltip : {
        show:false
    },
    series:[{
        type:"wordCloud",
        gridSize:1,
        sizeRange:[12,55],
        rotationRange:[-45,0,45,90],
        textStyle:{
            normal:{
                color:function () {
                    return 'rgb(' +
                            Math.round(Math.random()*255) +
                            ', ' +Math.round(Math.random()*255) +
                            ', ' +Math.round(Math.random()*255) +')'
                }
            }
        },
        right:null,
        bottom:null,
        data:data
    }]
}

//使用制定的配置项和数据显示图表
ec_right2.setOption(ec_right2_option);