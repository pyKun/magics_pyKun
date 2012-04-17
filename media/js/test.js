/* !
 * This is for dev test.
 *
 *
 *
 *
 *
 *
 */
function send_action(act, card) {
    var xmlhttp = new XMLHttpRequest();
    var role = document.getElementById('role').getAttribute('value');
    var action = act
    var url = "/dev/action/?player=" + role + "&action=" + action + '&card=' + card
    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            //alert(xmlhttp.responseText);
        }
    }
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
}
function get_status(){
    var stat = '0'
    var n = 100
    function validate_status(){
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function(){
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
            {
                // TODO use better json data
                stat = eval('(' + xmlhttp.responseText + ')').status;
                acts = eval('(' + xmlhttp.responseText + ')').actions;
                document.getElementById("status").innerHTML = stat;

                if (n>0){
                n = n -1
                do_actions(acts)
                // TODO use better time delay
                for (i=0;i<5000;i++){}
                validate_status();
                }
            }
        }
        xmlhttp.open("GET","/dev/status/?status="+stat,true);
        xmlhttp.send();
    }
    validate_status()
}

function do_actions(acts){
    l = acts.length
    for(i=0;i<l;i++){
        var current_player = document.getElementById('role').getAttribute('value');
        if (acts[i].player != current_player){
            // TODO move the card
            hk = $( "ul.gallery > li[id=" + acts[i].card + "]" )
            if ( acts[i].action == 'delete' ){
                del(hk)
            }else if( acts[i].action == 'recycle'){
                recycle(hk)
            }
        }
    }
}

function del( $item ) {
    $item.fadeOut(function() {
		var recycle_icon = "<a href='link/to/recycle/script/when/we/have/js/off' title='Recycle this image' class='ui-icon ui-icon-refresh'>Recycle image</a>";
        var $trash = $( "#trash" );
        var $list = $( "ul", $trash ).length ?
            $( "ul", $trash ) :
            $( "<ul class='gallery ui-helper-reset'/>" ).appendTo( $trash );

        $item.find( "a.ui-icon-trash" ).remove();
        $item.append( recycle_icon ).appendTo( $list ).fadeIn(function() {
            $item
                .animate({ width: "48px" })
                .find( "img" )
                    .animate({ height: "36px" });
        });
    });
}

function recycle( $item ) {
	var trash_icon = "<a href='link/to/trash/script/when/we/have/js/off' title='Delete this image' class='ui-icon ui-icon-trash'>Delete image</a>";
    var $gallery = $( "#gallery" );
    $item.fadeOut(function() {
        $item
            .find( "a.ui-icon-refresh" )
                .remove()
            .end()
            .css( "width", "96px")
            .append( trash_icon )
            .find( "img" )
                .css( "height", "72px" )
            .end()
            .appendTo( $gallery )
            .fadeIn();
    });
}
