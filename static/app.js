(function() {
    var Hanest = function (){
        var nudge = function () {
            setTimeout(function(){
                window.scrollTo(0,0);
            }, 1000)
        }

        var jump = function () {
            switch(location.hash) {
                case '#home':
                    document.body.className = 'home';
                    break;
                case '#newpost':
                    document.body.className = 'newpost';
                    break;
                case '#moeha':
                    document.body.className = 'moeha';
                    break;
            }
            nudge(); 
        }
        jump();
        window.addEventListener('hashchange', jump, false);
        window.addEventListener('orientationchange', nudge, false);
    }

    window.addEventListener('load', function(){
        new Hanest();
    }, false); 
})();


function emotion(emotion){
    console.log(emotion);
    document.getElementById("content").value += emotion;
    document.getElementById("emotion-select").options[0].selected  = true; 
}

function getName() {
    var namelist = new Array("江蛤蛤", "习包包", "康师傅", "奥观海", "天线宝",
    "金三胖", "斯大林", "元首","顺风快递", "查水表的");
    var value = namelist[Math.round(Math.random()*(namelist.length -1))];
    console.log(value);
    document.getElementById('username').value = value;
}