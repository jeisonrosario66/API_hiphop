//Update artist from backed, capture event
const btnHome = document.getElementById("redirect_button_home");
const urlArtist = "/artist"; // url
const rowsTable = document.getElementsByClassName("row_table_list_artist");

function requestAjax(dataSent, url) {
    $.ajax({
        url: url,
        type: "POST",
        data: { search: dataSent }, // This data is the artist name
        success: function(response) {
            // Update the dynamic content
            $("#dynamic-content").html(response);
            $("#search_input").val("");
        },
        error: function(error) {
            console.error('Error in the GET request:', error);
        }
    });
};
// ---------------------------------------------------------------------------------------------
// Function to handle the submit form
function handleFormSubmit(event) {
    event.preventDefault(); // avoid the form submit
    // If the input element is not empty -> request.AJAX
    if ($("#search_input").val() !== "") {
        // make an AJAX request to the server
        let searchInput = $("#search_input").val();
        requestAjax(searchInput, urlArtist);
    }
};

// Will handle of managed the form submit, it will only do it after uploading the entire document
$(document).ready(function() {
    $("#form_search_navbar").submit(handleFormSubmit);
});
btnHome.addEventListener("click", function() {
    // Redirige a la página de inicio
    window.location.href = "/";
});
// ---------------------------------------------------------------------------------------------

// ---------------------------------------------------------------------------------------------
// Add the click event to the each row in the table
for (const row of rowsTable) {
    row.addEventListener("click", function() {
        // Get data from the row
        let artistAka = row.cells[1].textContent;
        requestAjax(artistAka, urlArtist);
    });
};
// ---------------------------------------------------------------------------------------------
