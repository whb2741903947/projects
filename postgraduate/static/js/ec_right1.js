var ec_right1 = echarts.init(document.getElementById('right1'))

var ec_right1_option = {
    title : {
        text: '报考院校所在地',
        // subtext: '纯属虚构',
        x:'center',
        textStyle: {
            color:"white",
        },
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        x : 'left',
        y : 'center',
        orient:'vertical',
        data:["北上广等一线大城市","二三线城市","家乡所在城市","本科所在高校"],
        textStyle: {
            color:"white",
        },
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true, 
                type: ['pie', 'funnel']
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    series : [
        {
            name:'报考院校所在地',
            type:'pie',
            label : {
                show : false
            },
            radius : [50, 110],
            // center : ['75%', 200],
            roseType : 'area',
            x: '50%',               // for funnel
            max: 30,                // for funnel
            sort : 'ascending',     // for funnel
            data:[
                {value:40.59, name:'北上广等一线大城市'},
                {value:32.68, name:'二三线城市'},
                {value:18.72, name:'家乡所在城市'},
                {value:8.01, name:'本科所在高校'},
            ],
            color: ['#ff3333', '#ff9933', '#00ffcc', '#0099ff']
        }
    ]
};

//使用制定的配置项和数据显示图表
ec_right1.setOption(ec_right1_option);