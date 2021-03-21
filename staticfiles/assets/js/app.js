// app.js


/*
/// full screen for playing song
const fixedImage = document.getElementById('cp-fixed-image');
const removeOverlayScreen = document.getElementById('fullscreen-remove');
const screenOverlay = document.querySelector('.fullscreen-cp');
fixedImage.addEventListener('click', function(){
    if(!screenOverlay.classList.contains('display-overlay')){
        screenOverlay.classList.add('display-overlay');
    }
});
removeOverlayScreen.addEventListener('click', function(){
    if(screenOverlay.classList.contains('display-overlay')){
        screenOverlay.classList.remove('display-overlay');
    }
});

*/

//end full screen for playing song


// this object function should be instanciated
// only once throught out the program
// to prevent the more than one songs from playing 
// at the same time
var OnlySong = function(song){
    var instance;

    function createSong(){
        // get the source of the song
        const newSong = new Audio(song.src);
        return newSong;
    }
    return {
        getInstance: ()=> {
            if(!instance){
                instance = createSong();
            }
            return instance;
        }
    };    
}

var isAnyPlaying = false;
var currentlyPlaying;
var previouslyPlaying;

class SongPlayer{
    constructor(song){
        this.testSong = song;
        this.songInstance = new OnlySong(song);
        this.currentSong = this.songInstance.getInstance();
        this.isPlaying = false;
        this.parentDiv = this.getParentDiv();
        this.playIcon = this.getPlayIconElement();
        this.songDuration = this.parentDiv.querySelector('.song-duration');

        // remove all the child node from totalDuration element
        while (this.songDuration.hasChildNodes()) {
            this.songDuration.removeChild(this.songDuration.lastChild);
        }
        this.songDuration.appendChild(this.currentSong.duration);
    }
    getParentDiv(){
        return this.testSong.parentNode.parentNode;
    }
    getPlayIconElement(){
        return this.parentDiv.querySelector('.play-song');
    }
    play(){ 
        /* this is a private function 
        do not call it outside this class */
        this.currentSong.play();
        this.isPlaying = true;
        this.playIcon.classList.add('fa-pause');
        this.playIcon.classList.remove('fa-play');
        this.playIcon.classList.remove('fa-stop');
        console.log(this.totalDuration);
    }
    pause(){
        /* this is a private function 
        do not call it outside this class */
        this.currentSong.pause();
        this.isPlaying = false;
        this.playIcon.classList.add('fa-play');
        this.playIcon.classList.remove('fa-pause');
        this.playIcon.classList.remove('fa-stop');
    }
    stop(){
        /* this is a public function that can
        be called outside this class
        
        it will pause the song and set the currentTime to 
        zero */
        if(this.isPlaying){
            this.currentSong.pause();
            this.currentSong.currentTime = 0;
            this.isPlaying = false;
            console.log(this.currentSong.currentTime);
            // this.playIcon.classList.add('fa-stop');
            this.playIcon.classList.add('fa-play');
            this.playIcon.classList.remove('fa-pause');
        }
    }
    playpause(){
        if(!this.isPlaying){
            this.play();
        }else{
            this.pause();
        }
    }
} // end SongPlayer

function songIterator(start, end, step){
    nextSong;
    iterator = 1;
    
}

const allSongSrc = document.querySelectorAll('.song-src');
allSongSrc.forEach(function(song, index){
    
});
const allBtnPlay = document.querySelectorAll('.song-play-pause');

// var songToPlay;
allBtnPlay.forEach(function(btn, index){
    const song = allSongSrc[index];
    
    alert("It is working");
    alert(song);
    
        
    // the SongPlayer was instantiated outside 
    // the click eventListener sotthat there
    // will not be a new object each time the
    // button is clicked
    const songToPlay = new SongPlayer(song);
    btn.addEventListener('click', function(){
        
        if(!isAnyPlaying){
            // if there is no song playing, play it the song
            // and store it in a global variable
            // so that you can stop it.
            songToPlay.playpause();
            previouslyPlaying = songToPlay;
            
            isAnyPlaying = true;
        }else{
            // if the song playing previously is
            // not the same thing with what is currently playing
            // stop the previous one
            // but if it is the same thing, there is no
            // need to stop it. Just play or pause it normally
            if(!(previouslyPlaying == songToPlay)){
                previouslyPlaying.stop();
                songToPlay.playpause();
            }else if(previouslyPlaying == songToPlay){
                songToPlay.playpause();
            }

            previouslyPlaying = songToPlay;
        }
        
    });
});

/* end play song */



