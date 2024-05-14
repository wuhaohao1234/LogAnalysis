function refresh_msg() {
    layui.use(['jquery', 'popup'], function () {
        let $ = layui.jquery;
        let popup = layui.popup;
        $.ajax({
            type: "get",
            url: '/log_analysis/message/new_count',
            success: function (result) {
                if (result.success) {
                    popup.success('你有 ' + result.msg + '新消息，请查收！', function () {
                        $('#mine-nav-badge').text(result.msg);
                        if (!$('#nav-badge').hasClass('layui-hide')) {
                            return;
                        }
                        $('#nav-badge').removeClass('layui-hide');
                        $('#mine-nav-badge').removeClass('layui-hide');
                        $('#nav-msg-badge').text(result.msg);
                        $('#nav-msg-badge').removeClass('layui-hide');
                    })
                } else {
                    // popup.failure(result.msg, function () {
                    // });
                    $('#nav-badge').addClass('layui-hide');
                    $('#mine-nav-badge').addClass('layui-hide');
                    $('#nav-msg-badge').addClass('layui-hide');
                }
            }

        })
    })
}

setInterval(refresh_msg, 60000)