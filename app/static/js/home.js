var slideItems = document.querySelectorAll(".store__slide-item");
var btnNext = document.querySelector(".store__slide-btnNext");
var btnPrev = document.querySelector(".store__slide-btnPrev");
var dot = document.querySelectorAll(".store__slide-listDot i");

// slideshow :v
var currentIndex = 0;
function changeSlide(indexToShow) {
    if (indexToShow >= slideItems.length){
        indexToShow = 0;
    } else if(indexToShow < 0){
        indexToShow =  slideItems.length - 1;
    }
    slideItems[currentIndex].classList.add("hidden");
    slideItems[indexToShow].classList.remove("hidden");
    dot[currentIndex].classList.remove("dot__active");
    dot[indexToShow].classList.add("dot__active");
    currentIndex = indexToShow;
}

btnNext.addEventListener("click" , function(){
    changeSlide(currentIndex + 1);
})
btnPrev.addEventListener("click" , function(){
    changeSlide(currentIndex - 1);
})

function autoForward() {
    changeSlide(currentIndex + 1);
}
setInterval(autoForward, 3500);

for (let i = 0; i < dot.length ; i++){
    dot[i].addEventListener("click" , function(){
        changeSlide(i);
    })
}
