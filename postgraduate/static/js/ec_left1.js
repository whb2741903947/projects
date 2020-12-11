var ec_left1 = echarts.init(document.getElementById('left1'))

var ec_left1_option = {
    // 标题样式
    title: {
        text: '考研人数趋势',
        textStyle: {
            color:"white",
        },
        left:"center",
      },
      tooltip: {
        trigger: 'axis',
        // 指示器
        axisPointer: {
            type:'line',
            lineStyle: {
                color:"#7171C6"
            }
        },
      },
      legend: {
          data : ["考研人数"],
          left:"left"
      },

      // 图形位置  
      grid: {
        top: '50',
        left: '4%', 
        right: '6%',
        bottom: '4%',
        containLabel: true
    },
    xAxis: [{
        type: "category",
        axisLabel:{
            color:"white"
        },
        boundaryGap: false,
        data:["2016年","2017年","2018年","2019年","2020年"]
    }],
    yAxis: [{
        type:"value",
        // y轴字体设置
        axisLabel:{
            show:true,
            color:"white",
            fontSize:12,
            formatter:function(value){
                if (value>=1000) {
                    value = value / 1000 + 'k';
                }
                return value;
            }
        },
        // y轴设置显示
        axisLine:{
            show:true
        },
        // 与x轴平行的线样式
        splitLine:{
            show:true,
            lineStyle: {
                // color:"#17273B",
                width:1,
                type:"solid",
            }
        }
    }],
    series: [{
        name:"考研人数",
        type:"line",
        areaStyle: {},
        smooth:true,
        data:[177,201,238,290,341],
          itemStyle : { 
           color:{
                type: 'linear',
                x: 0,
                y: 0,
                x2: 0,
                y2: 1,
                colorStops: [{
                    offset: 0, color: '#1CD8D2' // 0% 处的颜色
                }, {
                    offset: 1, color: '#ffffff' // 100% 处的颜色
                }],
                global: false // 缺省为 false
           }
        },
    }],
    toolbox: {
        // show: true,
        feature: {
            // dataZoom: {
            //     yAxisIndex: 'none'
            // }, //区域缩放，区域缩放还原
            dataView: { 
                readOnly: false
            }, //数据视图
            magicType: {
                type: ['bar']
            },  //切换为折线图，切换为柱状图
            restore: {},  //还原
            saveAsImage: {}   //保存
        }
    }
};

//使用制定的配置项和数据显示图表
ec_left1.setOption(ec_left1_option);