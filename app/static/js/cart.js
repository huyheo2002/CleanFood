console.log("hello cart")

let updateBtns = document.getElementsByClassName("update-cart");

console.log("updateBtns", updateBtns);

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function (event) {
        let productId = event.target.getAttribute("data-product");
        let action = event.target.getAttribute("data-action");
        console.log("productId", productId, "action", action);
        console.log("user: ", user);

        if (user === "AnonymousUser") {
            console.log("user not logged in");
        } else {
            console.log("user logged in, success")
            updateUserOrder(productId, action);
        }
    });
}

function updateUserOrder(productId, action) {
    // console.log("user logged in, success add");
    // let url = "/update_item";

    // console.log("productId func", productId)
    // console.log("action func", action)

    fetch("/update_item", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({ "productId": productId, "action": action })
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log("data", data);
            location.reload();
        })
}

// function decreaseQuantity(button) {
//     const quantityElement = button.nextElementSibling;
//     let quantity = parseInt(quantityElement.textContent);
//     if (quantity > 1) {
//         quantity--;
//         quantityElement.textContent = quantity;
//         // Thực hiện các hành động khác sau khi giảm số lượng
//     }
// }

// function increaseQuantity(button) {
//     const quantityElement = button.previousElementSibling;
//     let quantity = parseInt(quantityElement.textContent);
//     quantity++;
//     quantityElement.textContent = quantity;
//     // Thực hiện các hành động khác sau khi tăng số lượng
// }
