document.querySelectorAll(".item_remove").forEach((button) => {

    button.addEventListener("click", function () {
        console.log(3)

        let productId = button.dataset.id;

    fetch("remove/",     {
      method: "POST",
      headers: {
        "X-CSRFToken": "{{ csrf_token }}",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `book_id=${productId}`,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          appendAlert(data.message, data.type);
        } else {
          appendAlert(data.message, data.type);
        }
      })
      .catch((error) => {
        appendAlert("An unexpected error occurred", "danger");
      });
  });
});
