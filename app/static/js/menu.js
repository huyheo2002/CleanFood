// // CART 
// let cart = new Cart();
// var btnToggleCart = document.querySelector(".btn__cart");
// var btnCloseCart = document.querySelector(".cart__btnClose");
// var btnResetCart = document.querySelector(".cart__footer-btnReset");

// btnToggleCart.onclick = function(){
//     cart.toggle();
//     cart.renderData();
// };

// btnCloseCart.onclick = function(){
//     cart.close();
// };
// btnResetCart.addEventListener("click", function(){
//     cart.reset();
//     cart.close();
// })

// SIDEBAR :v

// click sidebar show this list item it and hide list items other
// items in sidebar wrap subitems
const sidebarItemAll = document.querySelectorAll(".menu__itemsBlock");
// icon items in sidebar
const sidebarDotCoffee = document.querySelectorAll(".menu__dotCoffee");
// get text main in sidebar
const sidebarItemsTextAll = document.querySelectorAll(".menu__itemsBlock .menu__text");
// subitems in sidebar (get dot :V)
const sidebarSubItemAllDot = document.querySelectorAll(".menu__subnav-items");
// subitems in sidebar (text and show content)
const sidebarSubItemAll = document.querySelectorAll(".menu__subnav-items > a.menu__subnav-link");
const contentTitle = document.querySelectorAll(".title__itemTea");
const listProductsAll = document.querySelectorAll(".itemsHot__list");

// click items change color and show icon
// click items and show content
sidebarItemAll[0].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[0].classList.add("glow");
    sidebarDotCoffee[0].classList.add("visible");

    for(let i=0; i < contentTitle.length; i++){
        contentTitle[i].classList.remove("hide");
    }

    for(let i=0; i<listProductsAll.length; i++){
        listProductsAll[i].classList.remove("hide");
    }
})

sidebarItemAll[1].addEventListener("click", function(){
    resetAll();    
    contentTitle[0].classList.remove("hide");
    sidebarItemsTextAll[1].classList.add("glow");
    sidebarDotCoffee[1].classList.add("visible");
    contentTitle[1].classList.remove("hide");
    contentTitle[2].classList.remove("hide");
    // show product
    listProductsAll[0].classList.remove("hide");
    listProductsAll[1].classList.remove("hide");
    listProductsAll[2].classList.remove("hide");
})

sidebarItemAll[2].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[2].classList.add("glow");
    sidebarDotCoffee[2].classList.add("visible");
    contentTitle[3].classList.remove("hide");
    contentTitle[4].classList.remove("hide");
    // show product
    listProductsAll[3].classList.remove("hide");
    listProductsAll[4].classList.remove("hide");
})

sidebarItemAll[3].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[3].classList.add("glow");
    sidebarDotCoffee[3].classList.add("visible");
    contentTitle[5].classList.remove("hide");
    contentTitle[6].classList.remove("hide");
    // show product
    listProductsAll[5].classList.remove("hide");
    listProductsAll[6].classList.remove("hide"); 
})

sidebarItemAll[4].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[4].classList.add("glow");
    sidebarDotCoffee[4].classList.add("visible");
    contentTitle[7].classList.remove("hide");
    contentTitle[8].classList.remove("hide");
    contentTitle[9].classList.remove("hide");
    // show product
    listProductsAll[7].classList.remove("hide");
    listProductsAll[8].classList.remove("hide");    
    listProductsAll[9].classList.remove("hide");    
})

sidebarItemAll[5].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[5].classList.add("glow");
    sidebarDotCoffee[5].classList.add("visible");
    contentTitle[10].classList.remove("hide");
    contentTitle[11].classList.remove("hide");
    // show product
    listProductsAll[10].classList.remove("hide");
    listProductsAll[11].classList.remove("hide");    
})

// click subItems show content and glow text
sidebarSubItemAll[0].addEventListener("click", function(){
    // reset title and content all
    resetAll();
    // text(wrap subitems) main glow in sidebar
    sidebarItemsTextAll[1].classList.add("glow");
    // show icon text-main in sidebar
    sidebarDotCoffee[1].classList.add("visible");
    // text glow in sidebar
    sidebarSubItemAll[0].classList.add("glow");
    // dot glow in sidebar
    sidebarSubItemAllDot[0].classList.add("glow");
    // show title this content
    contentTitle[0].classList.remove("hide");
    // show items this content
    listProductsAll[0].classList.remove("hide");
})

sidebarSubItemAll[1].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[1].classList.add("glow");
    sidebarDotCoffee[1].classList.add("visible");
    sidebarSubItemAll[1].classList.add("glow");
    sidebarSubItemAllDot[1].classList.add("glow");    
    contentTitle[1].classList.remove("hide");
    listProductsAll[1].classList.remove("hide");
})

sidebarSubItemAll[2].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[1].classList.add("glow");
    sidebarDotCoffee[1].classList.add("visible");
    sidebarSubItemAll[2].classList.add("glow");
    sidebarSubItemAllDot[2].classList.add("glow");
    contentTitle[2].classList.remove("hide");
    listProductsAll[2].classList.remove("hide");
})

sidebarSubItemAll[3].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[2].classList.add("glow");
    sidebarDotCoffee[2].classList.add("visible");
    sidebarSubItemAll[3].classList.add("glow");
    sidebarSubItemAllDot[3].classList.add("glow");
    contentTitle[3].classList.remove("hide");
    listProductsAll[3].classList.remove("hide");
})

sidebarSubItemAll[4].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[2].classList.add("glow");
    sidebarDotCoffee[2].classList.add("visible");
    sidebarSubItemAll[4].classList.add("glow");
    sidebarSubItemAllDot[4].classList.add("glow");
    contentTitle[4].classList.remove("hide");
    listProductsAll[4].classList.remove("hide");
})

sidebarSubItemAll[5].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[3].classList.add("glow");
    sidebarDotCoffee[3].classList.add("visible");
    sidebarSubItemAll[5].classList.add("glow");
    sidebarSubItemAllDot[5].classList.add("glow");
    contentTitle[5].classList.remove("hide");
    listProductsAll[5].classList.remove("hide");
})

sidebarSubItemAll[6].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[3].classList.add("glow");
    sidebarDotCoffee[3].classList.add("visible");
    sidebarSubItemAll[6].classList.add("glow");
    sidebarSubItemAllDot[6].classList.add("glow");
    contentTitle[6].classList.remove("hide");
    listProductsAll[6].classList.remove("hide");
})

sidebarSubItemAll[7].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[4].classList.add("glow");
    sidebarDotCoffee[4].classList.add("visible");
    sidebarSubItemAll[7].classList.add("glow");
    sidebarSubItemAllDot[7].classList.add("glow");
    contentTitle[7].classList.remove("hide");
    listProductsAll[7].classList.remove("hide");
})

sidebarSubItemAll[8].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[4].classList.add("glow");
    sidebarDotCoffee[4].classList.add("visible");
    sidebarSubItemAll[8].classList.add("glow");
    sidebarSubItemAllDot[8].classList.add("glow");
    contentTitle[8].classList.remove("hide");
    listProductsAll[8].classList.remove("hide");
})

sidebarSubItemAll[9].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[4].classList.add("glow");
    sidebarDotCoffee[4].classList.add("visible");
    sidebarSubItemAll[9].classList.add("glow");
    sidebarSubItemAllDot[9].classList.add("glow");
    contentTitle[9].classList.remove("hide");
    listProductsAll[9].classList.remove("hide");
})

sidebarSubItemAll[10].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[5].classList.add("glow");
    sidebarDotCoffee[5].classList.add("visible");
    sidebarSubItemAll[10].classList.add("glow");
    sidebarSubItemAllDot[10].classList.add("glow");
    contentTitle[10].classList.remove("hide");
    listProductsAll[10].classList.remove("hide");
})

sidebarSubItemAll[11].addEventListener("click", function(){
    resetAll();
    sidebarItemsTextAll[5].classList.add("glow");
    sidebarDotCoffee[5].classList.add("visible");
    sidebarSubItemAll[11].classList.add("glow");
    sidebarSubItemAllDot[11].classList.add("glow");
    contentTitle[11].classList.remove("hide");
    listProductsAll[11].classList.remove("hide");
})

function resetAll(){
    // reset content title
    for(let i=0; i < contentTitle.length; i++){
        contentTitle[i].classList.add("hide");
    }

    // reset color sub-text in sidebar
    for(let i=0; i < sidebarSubItemAll.length; i++){
        sidebarSubItemAll[i].classList.remove("glow");
    }

    // reset dot glow in sidebar
    for(let i=0; i < sidebarSubItemAllDot.length; i++){
        sidebarSubItemAllDot[i].classList.remove("glow");
    }

    // reset text-main glow in sidebar
    for(let i=0; i< sidebarItemsTextAll.length; i++){
        sidebarItemsTextAll[i].classList.remove("glow");
    }

    // reset icon text-main in sidebar
    for(let i=0; i< sidebarDotCoffee.length; i++){
        sidebarDotCoffee[i].classList.remove("visible");
    }
    
    // reset product
    for(let i=0; i<listProductsAll.length; i++){
        listProductsAll[i].classList.add("hide");
    }
}
