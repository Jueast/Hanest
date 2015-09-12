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