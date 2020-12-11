// 本js 为数据控制文件
function get_center2_data(){
    $.ajax({
        url:"/center2",
        success:function(data) {
            ec_center_option.series[0].data=data.data
            ec_center.setOption(ec_center_option)
        },
        error:function(xhr,type,errorThrown){

        }
    })
}

function get_wordcloud_data() {
    $.ajax({
        url:"/right2",
        success:function(data) {
            ec_right2_option.series[0].data=data.data;
            ec_right2.setOption(ec_right2_option);
    }
    })
}

function get_rate_data() {
    $.ajax({
        url:"/left2",
        success:function(data) {
            ec_left2_option.series[0].data[0].value=data.data;
            ec_left2.setOption(ec_left2_option);
    }
    })
}

function unmeaning() {
    $.ajax({
        url:"/ques",
        success:function(data) {
            pass;
    }
    })
}

function gettime(){
    $.ajax({
        url:"/time",
        timeout:10000, //超时时间设置为10秒
        success:function(data){
            $("#tim").html(data)
        },
        error:function(xhr,type,errorThrown){

        }
    });
}

function get_c1_data(){
    $.ajax({
        url:"/c1",
        success:function(data){
            $(".num h1").eq(0).text(data.confirm);
            $(".num h1").eq(1).text(data.suspect);
            $(".num h1").eq(2).text(data.heal);
            $(".num h1").eq(3).text(data.dead);
        },
        error:function(xhr,type,errorThrown){

        }
    });
}

get_center2_data()
get_rate_data()
setInterval(get_rate_data,1000*600)
setInterval(unmeaning,1000*1200)
setInterval(get_wordcloud_data,1000*1800)
setInterval(gettime,1000)
setInterval(get_c1_data,1000)