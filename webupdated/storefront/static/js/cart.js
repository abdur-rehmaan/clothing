document.addEventListener("DOMContentLoaded", () => {
  const addToCartButtons = document.querySelectorAll(".add-to-cart-button");

  
  addToCartButtons.forEach(button => {
    button.addEventListener("click", function() {
      const productId = this.getAttribute("data-product-id");
      addToCart(productId);
    });
  });
}); 

function addToCart(productId){
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  
  // Check if the product is already in the cart
  const existingItem = cart.find(item => item.id === productId);
  if (existingItem) {
    existingItem.quantity++;
  } else {
    cart.push({ id: productId, quantity: 1 });
  }
  
  localStorage.setItem("cart", JSON.stringify(cart));
  $('.add-to-cart-button').click(function() {
    const productId = $(this).data('product-id');
    
    // Prepare data for the request (e.g., product ID and quantity)
    const cartData = [
      {
        id: productId,
        quantity: 1,  // You can adjust the quantity as needed
      }
    ];
  

  $.ajax({
    type: 'POST',
    url: '/add_to_cart/',  // Update the URL as needed
    data: JSON.stringify(cartData),
    contentType: 'application/json',
    headers: {
      'X-CSRFToken': csrfToken  // Make sure to set the CSRF token
    },
    success: function(data) {
      // Handle the success response if needed
      console.log(data.message);
      
      // You can also update the UI to reflect the added item
    },
    error: function(textStatus, errorThrown) {
      // Handle errors if needed
      console.error('Error adding item to cart:', textStatus, errorThrown);
    }

  });
});
}
// Inside your cart.js script
document.addEventListener("DOMContentLoaded", () => {
  const removeFromCartButtons = document.querySelectorAll(".remove-from-cart-button");

  removeFromCartButtons.forEach(button => {
    button.addEventListener("click", function() {
      const productId = this.getAttribute("data-product-id");
      removeFromCart(productId);
    });
  });
});

function removeFromCart(productId) {
  // Send data to the server to remove the item from the cart
  $.ajax({
    type: 'POST',
    url: '/remove_from_cart/',  // Update the URL as needed
    data: JSON.stringify({ id: productId }),
    contentType: 'application/json',
    headers: {
      'X-CSRFToken': csrfToken
    },
    success: function(data) {
      // Handle success response if needed
      console.log(data.message);
      // You can update the UI to reflect the removal of the item
      // For example, remove the item from the cart displayed on the page
    },
    error: function(textStatus, errorThrown) {
      // Handle errors if needed
      console.error('Error removing item from cart:', textStatus, errorThrown);
    }
  });
}
