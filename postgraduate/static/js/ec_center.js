var ec_center = echarts.init(document.getElementById('center2'));

// var mydata = [{'name': '北京', 'value': 223}, {'name': '上海', 'value': 65}, {'name': '江苏', 'value': 63}, {'name': '陕西', 'value': 62}, {'name': '湖北', 'value': 58}, {'name': '辽宁', 'value': 51}, {'name': '山东', 'value': 41}, {'name': '四川', 'value': 41}, {'name': '广东', 'value': 40}, {'name': '河北', 'value': 33}, 
// {'name': '河南', 'value': 31}, {'name': '黑龙江', 'value': 28}, {'name': '天津', 'value': 28}, {'name': '浙江', 'value': 27}, {'name': '吉林', 'value': 26}, {'name': '安徽', 'value': 25}, {'name': '湖南', 'value': 23}, {'name': '甘肃', 'value': 19}, {'name': '重庆', 'value': 19}, {'name': '云南', 'value': 18}, 
// {'name': '山西', 'value': 16}, {'name': '福建', 'value': 16}, {'name': '江西', 'value': 16}, {'name': '广西', 'value': 14}, {'name': '新疆', 'value': 14}, {'name': '内蒙古', 'value': 11}, {'name': '贵州', 'value': 10}, {'name': '香港', 'value': 8}, {'name': '青海', 'value': 5}, {'name': '宁夏', 'value': 4}, {'name': '海南', 'value': 4}, {'name': '西藏', 'value': 3}]


var ec_center_option = {
    title: {
        text: '',
        subtext: '',
        x:'left'
    },
    tooltip : {
        trigger: 'item'
    },  

    //左侧小导航图标
    visualMap: {
        show : true,
        x: 'left',
        y: 'bottom',
        textStyle:{
            fontStyle:8,
            color:"white"
        },
        splitList: [
            {start: 1, end:9},{start: 10, end: 19},
            {start: 20, end: 39},{start: 40, end: 99},
            {start: 100},
        ],
        color: ['#F6471D', '#F6B61D', '#F7F920','#C5F57E', '#FFFAFA']
    },  

    //配置属性
    series: [{
        name: '考研学校数量',
        type: 'map',
        mapType: 'china',
        roam: false,  //拖动和缩放
        itemStyle:{
            normal:{
                borderWidth:.5, //区域边框宽度
                borderColor:"#009fe8", //区域边框颜色
                areaColor:"#ffefd5", //区域颜色
            },
            emphasis:{  //鼠标滑过地图高亮的相关设置
                borderWidth:.5, //区域边框宽度
                borderColor:"#4b0082", //区域边框颜色
                areaColor:"#fff", //区域颜色
            }
        },
        label: {
            normal: {
                show: true,  //省份名称
                fontSize:8,
            },
            emphasis: {
                show: true,
                fonSize:8,
            }
        },
        data:[], //数据
    }]
};

//使用制定的配置项和数据显示图表
ec_center.setOption(ec_center_option);