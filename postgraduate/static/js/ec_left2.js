var ec_left2 = echarts.init(document.getElementById('left2'))

// var data = 50

var ec_left2_option = {
    // 标题样式
    title: {
        text: '考研女生占比',
        textStyle: {
            color:"white",
        },
        left:"left",
      },
    tooltip: {
        formatter: "{a} <br/>{b} : {c}%"
    },
    toolbox: {
        show: true,
        feature: {
            mark: {
                show: true
            },
            restore: {
                show: true
            },
            saveAsImage: {
                show: true
            }
        }
    },
    series: [
        {
            startAngle: 340, //开始角度 左侧角度
            endAngle: 0, //结束角度 右侧
            name: '考研',
            type: 'gauge',
            detail: {
              offsetCenter: [0,"30%"],    //设置仪表盘下方显示内容位置
              formatter:'{value}%',
              textStyle:{color:'white',fontSize:22},
              },
            title : {               //设置仪表盘中间显示文字样式
                textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                    fontWeight: 'bolder',
                    fontSize: 13,
                    fontStyle: 'italic',
                    color:"#00ffcc"
                }
            },
            data: [{
                value: [], 
                name: '女生占比',
              }],
            center: ["47%", "45%"], // 默认全局居中
            splitLine : {           //分割线样式（及10、20等长线样式）
               length : 15,
               lineStyle: {            // 分隔线样式。
                color: "#eee",              //线的颜色,默认 #eee。
                opacity: 1,                 //图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
                width: 2,                   //线度,默认 2。
                type: "solid",              //线的类型,默认 solid。 此外还有 dashed,dotted
                shadowBlur: 10,             //(发光效果)图形阴影的模糊大小。该属性配合 shadowColor,shadowOffsetX, shadowOffsetY 一起设置图形的阴影效果。 
                shadowColor: "#fff",        //阴影颜色。支持的格式同color。
            }
            },
            pointer : { //指针样式
              length: '80%'
            },
            axisLine:{
              show : true,// 是否显示仪表盘轴线(轮廓线),默认 true。
              lineStyle : { // 属性lineStyle控制线条样式
                shadowBlur: 10,             //(发光效果)图形阴影的模糊大小。该属性配合 shadowColor,shadowOffsetX, shadowOffsetY 一起设置图形的阴影效果。 
                shadowColor: "#fff",        //阴影颜色。支持的格式同color。
                  // color : [ //表盘颜色
                  //     [ 0.5, "#DA462C" ],//0-50%处的颜色
                  //   [ 0.7, "#FF9618" ],//51%-70%处的颜色
                  //   [ 0.9, "#FFED44" ],//70%-90%处的颜色
                  //   [ 1,"#20AE51" ]//90%-100%处的颜色
                  // ],
                  width : 15//表盘宽度
              }
          },
          axisLabel : { //文字样式（及“10”、“20”等文字样式）
            //   color : "white",
              distance : 5 //文字离表盘的距离
          },
        }
    ]
};

//使用制定的配置项和数据显示图表
ec_left2.setOption(ec_left2_option);